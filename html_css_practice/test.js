const video = document.getElementById('myVideo');
const playPauseButton = document.getElementById('playPause');
const muteUnmuteButton = document.getElementById('muteUnmute');

playPauseButton.addEventListener('click', function() {
    if (video.paused || video.ended) {
        video.play();
        playPauseButton.textContent = 'Pause';
    } else {
        video.pause();
        playPauseButton.textContent = 'Play';
    }
});

muteUnmuteButton.addEventListener('click', function() {
    if (video.muted) {
        video.muted = false;
        muteUnmuteButton.textContent = 'Mute';
    } else {
        video.muted = true;
        muteUnmuteButton.textContent = 'Unmute';
    }
});
