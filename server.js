// Intentionally vulnerable Node.js for testing CodeQL code scanning.
// DO NOT use any of this in real code.

const express = require("express");
const { exec } = require("child_process");
const app = express();

app.get("/run", (req, res) => {
  // CWE-78: command injection from untrusted query param
  const dir = req.query.dir;
  exec("ls " + dir, (err, stdout) => res.send(stdout));
});

app.get("/calc", (req, res) => {
  // CWE-94: code injection via eval
  const expr = req.query.expr;
  res.send(String(eval(expr)));
});

app.get("/redirect", (req, res) => {
  // CWE-601: open redirect from untrusted input
  res.redirect(req.query.url);
});

app.listen(3000);
