const WebSocket = require("ws"); // Import WebSocket package for Node.js

const socket = new WebSocket("ws://localhost:5000/ws");

socket.on("open", () => {
    console.log("✅ Connected to WebSocket Server");
    socket.send("Hello from Node.js WebSocket client!");
});

socket.on("message", (data) => {
    console.log("📩 Received:", data.toString());
});

socket.on("error", (error) => {
    console.error("⚠ WebSocket Error:", error);
});

socket.on("close", () => {
    console.log("🔌 WebSocket Disconnected");
});

