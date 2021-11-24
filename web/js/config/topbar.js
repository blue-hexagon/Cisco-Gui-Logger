topbar.config({
    autoRun: true,
    barThickness: 5,
    barColors: {
        '0': 'rgba(8,255,204,0.7)',
        '.3': 'rgb(50,36,255)',
        '1.0': 'rgb(255,0,0)'
    },
    shadowBlur: 5,
    shadowColor: 'rgba(0, 0, 0, .7)',
    className: 'topbar',
})
topbar.show();
(function step() {
    setTimeout(function () {
        if (topbar.progress('+.01') < 1) step()
    }, 16)
})()
$(function () {
    topbar.hide()
})