import React from "react";
import "./App.css";
import FreeSolo from "./components/home/selection";
import Stack from "@mui/material/Stack";
import Button from "@mui/material/Button";
import { Alert } from "@mui/material";
import { red } from "@mui/material/colors";

export default function App() {
  return (
    <div
      className="d-flex align-items-center justify-content-center bg"
      style={{ height: "100vh" }}
    >
      <div className="p-4 bg-white  border border-light rounded m-5" style={{}}>
        {/* <div className="p-4 border border-light rounded m-5" style={{}}> */}
        <Stack spacing={2} sx={{}}>
          <FreeSolo />
          <Alert severity="success" color="info">
            This is a success alert — check it out!
          </Alert>
          <div className="d-flex justify-content-center">
            <Button variant="contained">Contained</Button>
          </div>
        </Stack>
      </div>
    </div>
  );
}
