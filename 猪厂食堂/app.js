//app.js
const AV = require('./utils/av-weapp-min.js');
App({
  onLaunch: function () {
    // 展示本地存储能力
    AV.init({
      appId: 'MrPxk72DQXNXcaUs1sQcpH4i-gzGzoHsz',
      appKey: 'saEUWKWsA8NmedsX8Y17wrU0',
    });

    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
  },
  globalData: {
    userInfo: null
  }
})