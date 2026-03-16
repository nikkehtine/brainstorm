import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "brAInstorm" },
    { name: "description", content: "Welcome to brAInstorm!" },
  ];
}

export default function Home() {
  return <Welcome />;
}
