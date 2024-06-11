import "./style.css";
import Trame from "@kitware/trame";
import { setupCounter } from "./counter.js";

document.querySelector("#app").innerHTML = `
  <div>
    <h1>Hello Trame !</h1>
    <div class="card">
    <button id="counter" type="button"></button>
    <button id="play" type="button">Auto update</button>
    <button id="subtract" type="button">-1</button>
    <button id="random" type="button">Random</button>
    </div>
  </div>
`;

const trame = new Trame();
trame.connect().then(() => {
  setupCounter(document.querySelector("#counter"), trame);
  trame.refs["counter"] = {
    reset(value) {
      trame.state.set("count", value);
    },
  };
  document
    .querySelector("#play")
    .addEventListener("click", () => trame.trigger("toggle_play"));
  document
    .querySelector("#subtract")
    .addEventListener("click", () => trame.trigger("subtract"));
  document
    .querySelector("#random")
    .addEventListener("click", () => trame.trigger("random"));
});
