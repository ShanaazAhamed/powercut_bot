import * as React from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { grey, pink } from "@mui/material/colors";
import Avatar from "@mui/material/Avatar";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

export default function BasicStack() {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container
        maxWidth="sm"
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%,-50%)",
        }}
      >
        <Box
          sx={{
            height: "50vh",
            border: "1px solid",
            borderColor: grey[300],
            backgroundColor: grey[50],
          }}
        >
          <Avatar sx={{ bgcolor: grey, margin: "50px auto" }}>
            <AccountCircleIcon />
          </Avatar>
          <Container sx={{ alignSelf: "center" }}>
            <Box
              component="form"
              sx={{
                "& > :not(style)": {
                  m: 1,
                  width: "25ch",
                },
              }}
              noValidate
              autoComplete="off"
            >
              <TextField
                sx={{ alignSelf: "center" }}
                id="outlined-basic"
                label="Enter your ID"
                variant="outlined"
              />
            </Box>
            <Button variant="contained" sx={{ alignSelf: "center" }}>
              Outlined
            </Button>
          </Container>
        </Box>
      </Container>
    </React.Fragment>
  );
}
