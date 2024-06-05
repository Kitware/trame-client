export function setupCounter(element, trame) {
  trame.state.watch(["count"], (count) => {
    element.innerHTML = `count is ${count}`;
  });
  element.addEventListener("click", () => trame.trigger("add"));
}
