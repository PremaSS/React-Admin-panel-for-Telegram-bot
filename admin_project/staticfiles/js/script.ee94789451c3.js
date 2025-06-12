document.addEventListener('DOMContentLoaded', function () {
  const exploreBtn = document.getElementById('explore-btn');

  if (exploreBtn) {
    exploreBtn.addEventListener('click', function (event) {
      event.preventDefault();
      window.location.href = '/explore/';
    });
  }
});
