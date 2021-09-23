'use strict';

var electron = require('electron');

electron.app.whenReady().then(function () {
  new electron.BrowserWindow({
    width: 800,
    height: 600
  });
});
