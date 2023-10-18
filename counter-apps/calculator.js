function calculate() {
  const a = document.getElementById("a").value;
  const b = document.getElementById("b").value;
  fetch(`/calculate.py?a=${a}&b=${b}`)
    .then((response) => response.text())
    .then((result) => {
      document.getElementById("result").innerText = `Result: ${result}`;
    });
}
