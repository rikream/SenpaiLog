document.addEventListener("DOMContentLoaded", function () {

  const app = document.getElementById("app");
  const id = new URLSearchParams(location.search).get("id");

  // =========================
  // 🎬 DETAILS PAGE
  // =========================
  if (id) {
    fetch(`https://api.jikan.moe/v4/anime/${id}`)
      .then(res => res.json())
      .then(data => {
        const a = data.data;

        app.innerHTML = `
          <div class="details">
            <h1>${a.title}</h1>
            <img src="${a.images.jpg.image_url}">
            <p>⭐ ${a.score}</p>
            <p>${a.synopsis}</p>
            <a href="/anime/browse/" class="back-btn">⬅ Back</a>
          </div>
        `;
      })
      .catch(() => {
        app.innerHTML = "<p>Error loading details 😢</p>";
      });

    return;
  }

  // =========================
  // 📺 MAIN PAGE UI
  // =========================
  app.innerHTML = `
    <div class="controls">
      <input id="searchInput" placeholder="🔍 Search anime">

      <select id="genreFilter">
        <option value="all">All Genres</option>
      </select>

      <select id="sortFilter">
        <option value="rank">Sort by Rank</option>
        <option value="rating">Sort by Rating</option>
      </select>

      <button id="randomBtn">🎲 Random</button>
    </div>

    <div id="animeGrid" class="grid"></div>

    <button id="loadMoreBtn" class="load-more">Load More</button>
  `;

  const grid = document.getElementById("animeGrid");
  const searchInput = document.getElementById("searchInput");
  const genreFilter = document.getElementById("genreFilter");
  const sortFilter = document.getElementById("sortFilter");
  const randomBtn = document.getElementById("randomBtn");
  const loadMoreBtn = document.getElementById("loadMoreBtn");

  let animeData = [];
  let currentPage = 1;
  let isLoading = false;

  // =========================
  // LOAD DATA (PAGINATION)
  // =========================
  async function loadAnime() {
    if (isLoading) return;

    isLoading = true;
    loadMoreBtn.textContent = "Loading...";

    try {
      const res = await fetch(`https://api.jikan.moe/v4/top/anime?page=${currentPage}`);
      const json = await res.json();

      animeData = animeData.concat(json.data);

      populateGenres();
      applyFilters();

      currentPage++;

      loadMoreBtn.textContent = "Load More";

    } catch {
      loadMoreBtn.textContent = "Failed 😢";
    }

    isLoading = false;
  }

  // =========================
  // GENRES (NO DUPLICATES)
  // =========================
  function populateGenres() {
    const existing = new Set(
      Array.from(genreFilter.options).map(o => o.value)
    );

    animeData.forEach(a => {
      a.genres.forEach(g => {
        if (!existing.has(g.name)) {
          const o = document.createElement("option");
          o.value = g.name;
          o.textContent = g.name;
          genreFilter.appendChild(o);
          existing.add(g.name);
        }
      });
    });
  }

  // =========================
  // RENDER
  // =========================
  function render(list) {
    grid.innerHTML = "";

    list.forEach(a => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <img src="${a.images.jpg.image_url}">
        <h3>#${a.rank} ${a.title}</h3>
        <p>⭐ ${a.score ?? "N/A"}</p>
        <a href="?id=${a.mal_id}" class="view-btn">View</a>
      `;

      grid.appendChild(card);
    });
  }

  // =========================
  // FILTERS
  // =========================
  function applyFilters() {
    let list = [...animeData];

    if (searchInput.value) {
      list = list.filter(a =>
        a.title.toLowerCase().includes(searchInput.value.toLowerCase())
      );
    }

    if (genreFilter.value !== "all") {
      list = list.filter(a =>
        a.genres.some(g => g.name === genreFilter.value)
      );
    }

    if (sortFilter.value === "rating") {
      list.sort((a, b) => (b.score || 0) - (a.score || 0));
    } else {
      list.sort((a, b) => a.rank - b.rank);
    }

    render(list);
  }

  // =========================
  // EVENTS
  // =========================
  searchInput.oninput = applyFilters;
  genreFilter.onchange = applyFilters;
  sortFilter.onchange = applyFilters;

  randomBtn.onclick = () => {
    const r = animeData[Math.floor(Math.random() * animeData.length)];
    location.href = `?id=${r.mal_id}`;
  };

  loadMoreBtn.onclick = loadAnime;

  // =========================
  // INIT
  // =========================
  loadAnime(); // first load

});