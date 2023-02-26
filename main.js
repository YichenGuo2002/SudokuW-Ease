const { app, BrowserWindow} = require('electron')
const path = require('path')
// 设置菜单栏, win是窗口实例


function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

const menuTemplate = [{
    label: '主页',
    click() {
      // 页面跳转方式一（推荐）
      mainWindow.webContents.send('href', '/index');
      // 页面跳转方式二
      // mainWindow.loadURL(winURL+'#/index')
    }
  },
  {
    label: '测试页',
    submenu: [
      {
        label: '第1页',
        click() {
          mainWindow.webContents.send('href', '/page1');
        }
      },
      {
        label: '第2页',
        click() {
          mainWindow.webContents.send('href', '/page2');
        }
      }
    ]
  }
  ];
  
  var Menu = require('electron').Menu;
  Menu.setApplicationMenu( Menu.buildFromTemplate(menuTemplate));