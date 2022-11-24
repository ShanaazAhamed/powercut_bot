import React from "react";
import "./App.css";
import FreeSolo from "./components/home/selection";
import Stack from "@mui/material/Stack";
import Button from "@mui/material/Button";
import { Alert, Icon } from "@mui/material";
import { red } from "@mui/material/colors";
import { Search } from "@mui/icons-material";

export default function App() {
  return (
    <div
      className="d-flex align-items-center justify-content-center bg"
      style={{ height: "100vh" }}
    >
      <div className="p-5  rounded m-5" style={{}} id="container">
        {/* <div className="p-4 border border-light rounded m-5" style={{}}> */}
        <Stack spacing={2} sx={{ width: "40vw" }}>
          <FreeSolo />
          <Alert icon={false} className="mx-auto">
            You belongs to Group : C
          </Alert>
          <div className="d-flex justify-content-center">
            <Button variant="contained" sx={{}}>
              Search
              <Search className="pw-5" />
            </Button>
          </div>
        </Stack>
      </div>
    </div>
  );
}
