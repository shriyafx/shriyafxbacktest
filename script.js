let replayRunning = false;

function startReplay() {
    if (replayRunning) return;

    replayRunning = true;
    alert("Replay started!");
}

function pauseReplay() {
    replayRunning = false;
    alert("Replay paused!");
}

function resetReplay() {
    replayRunning = false;
    alert("Replay reset!");
}
document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("playBtn").addEventListener("click", startReplay);

    document.getElementById("pauseBtn").addEventListener("click", pauseReplay);

    document.getElementById("resetBtn").addEventListener("click", resetReplay);

});
