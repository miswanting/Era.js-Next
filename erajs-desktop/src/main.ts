import { app, BrowserWindow } from 'electron'
app.whenReady().then(function () {
  const bw = new BrowserWindow({
    width: 800,
    height: 600
  })
})