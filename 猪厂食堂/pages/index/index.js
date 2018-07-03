//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: '豚（zhu）厂食记',
  },
  goToPage:function(param){
    wx.navigateTo({
      url: '/pages/eatWhat/eatWhat',
    })
  },
})
