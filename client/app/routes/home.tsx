import { Welcome } from "../welcome/welcome";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "brAInstorm" },
    { name: "description", content: "Welcome to brAInstorm!" },
  ];
}

export default function Home() {
  return <Welcome />;
}
