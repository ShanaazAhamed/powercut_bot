import React from "react";
import SelectTextFields from "./components/home/selection";
import Title from "./components/home/title";

export default function App() {
  return (
    <div
      className="d-flex align-items-center justify-content-center flex-column"
      style={{ height: "100vh" }}
    >
      <div>
        <SelectTextFields />
      </div>
      <div>
        <SelectTextFields />
      </div>
    </div>
  );
}
