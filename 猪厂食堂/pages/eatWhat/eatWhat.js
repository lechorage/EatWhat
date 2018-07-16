// pages/eatWhat/eatWhat.js
const app = getApp()
const AV = require('../../utils/av-weapp-min.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    eats:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var d = new Date()
    var year = d.getFullYear()
    var month = d.getMonth() + 1
    var date = d.getDate()
    var index = year + "-" + ('0' + month).slice(-2) + "-" + ('0' + date).slice(-2)
    var query = new AV.Query('Eat');
    query.equalTo("YMD", index)
      .find()
      .then((eats) => {
        this.setData({ eat: eats[0], id: options.id })
      })
    
  },
 
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})