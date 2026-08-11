const API_BASE = "http://localhost:5000";

async function doSignup() {
// TODO: Read name, email, username and password from the form inputs

// TODO: Validate the fields, then POST { name, email, username, password } to /register
// TODO: Handle success (redirect to login.html) and failure appropriately

const fname = document.getElementById("fname").value.trim();
const lname = document.getElementById("lname").value.trim();
const name = fname + lname;
const email = document.getElementById("email").value.trim();
const username = document.getElementById("username").value.trim();
const password = document.getElementById("password").value.trim();
const errorEl = document.getElementById("login-error");
errorEl.style.display = "none";

if (!username || !password || !fname || !lname || !email) {
showError("Please fill in all fields.");
return;
}

try {
const res = await fetch(`${API_BASE}/register`, {
method: "POST",
headers: { "Content-Type": "application/json" },
credentials: "include",
body: JSON.stringify({ username, password, name, email }),
});
const data = await res.json();

if (!res.ok) {
showError(data.error || "Registration failed.");
return;
}
window.location.href = "index.html";
} catch (e) {
showError("Could not connect to the server. Is the backend running?");
}
}

document.addEventListener("keydown", (e) => { if (e.key === "Enter") doSignup(); });