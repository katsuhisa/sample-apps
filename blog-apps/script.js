async function loadPosts() {
  const response = await fetch("/get-posts.php");
  const posts = await response.json();
  const container = document.getElementById("blog-posts");
  container.innerHTML = posts
    .map((post) => `<p>${post.title}: ${post.content}</p>`)
    .join("");
}
