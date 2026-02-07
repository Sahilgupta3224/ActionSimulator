import * as PIXI from "https://cdn.jsdelivr.net/npm/pixi.js@8/dist/pixi.min.mjs";

PIXI.Assets.setPreferences({
  texture: {
    scaleMode: PIXI.SCALE_MODES.NEAREST
  }
});

const app = new PIXI.Application();

await app.init({
  width: 800,
  height: 600,
  backgroundColor: 0x1e1e1e
});

document.body.appendChild(app.canvas);

await PIXI.Assets.load("./assets/Pixi_boy_football.json");
const sheet = PIXI.Assets.get("./assets/Pixi_boy_football.json");

const animations = {
  idle: sheet.animations["idle"],
  run: sheet.animations["run"],
  celebrate: sheet.animations["celebrate"],
  kick: sheet.animations["kick"],
  walk: sheet.animations["walk"],
  turn: sheet.animations["turn"]
};

const player = new PIXI.AnimatedSprite(animations.idle);
player.anchor.set(0.5);
player.x = app.screen.width / 2;
player.y = app.screen.height / 2;
player.animationSpeed = 0.1;
player.play();

app.stage.addChild(player);

let currentAnim = "idle";

function playAnimation(name, loop = true, speed = 0.1) {
  if (currentAnim === name) return;

  player.textures = animations[name];
  player.loop = loop;
  player.animationSpeed = speed;
  player.play();

  currentAnim = name;
}

window.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") playAnimation("run", true, 0.15);
  if (e.key === " ") playAnimation("celebrate", false, 0.12);
});

window.addEventListener("keyup", () => {
  playAnimation("idle");
});

window.player = player;
window.playAnimation = playAnimation;
