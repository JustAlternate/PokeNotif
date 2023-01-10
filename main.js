const { app, BrowserWindow, Notification } = require('electron')

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600
  })

  win.loadFile('index.html')
}



function showNotification () {
  const NOTIFICATION_TITLE = 'Welcome to PokeNotif'
  const NOTIFICATION_BODY = 'This is your very first PokeNotif notification, make sure to hit the \'OK\' button to proceed to the next notification'
  new Notification({ title: NOTIFICATION_TITLE, body: NOTIFICATION_BODY }).show()
}

app.whenReady().then(createWindow).then(showNotification)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})