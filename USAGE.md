# 使用指南

本文档将帮助您快速上手使用Public APIs中文版。

## 🔍 如何查找API

### 1. 使用分类索引
点击[分类索引](ReadMe.md#分类索引)中的任何分类，快速跳转到相关API列表。

### 2. 页面内搜索
- 按 `Ctrl+F` (Windows/Linux) 或 `Cmd+F` (Mac)
- 输入关键词进行搜索
- 支持中文和英文关键词

### 3. 按需求筛选
根据以下条件筛选API：
- **认证方式**：选择无需认证(`No`)或需要API密钥的服务
- **HTTPS支持**：确保数据传输安全
- **CORS支持**：前端直接调用的必要条件

## 📖 理解API信息

### 字段说明
| 字段 | 含义 | 示例 |
|:---|:---|:---|
| **API** | API名称和文档链接 | [OpenWeatherMap](https://openweathermap.org/api) |
| **描述** | API功能简介 | 天气API |
| **认证** | 认证要求 | `apiKey` |
| **HTTPS** | 是否支持HTTPS | Yes |
| **CORS** | 跨域支持 | Yes |

### 认证方式详解

#### `No` - 无需认证
```javascript
// 直接调用，无需任何认证
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data));
```

#### `apiKey` - API密钥认证
```javascript
// 需要注册获取API密钥
const apiKey = 'your-api-key';
fetch(`https://api.example.com/data?key=${apiKey}`)
  .then(response => response.json())
  .then(data => console.log(data));
```

#### `OAuth` - OAuth认证
```javascript
// 需要OAuth流程获取访问令牌
const token = 'your-access-token';
fetch('https://api.example.com/data', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

#### `User-Agent` - 用户代理认证
```javascript
// 需要设置User-Agent头
fetch('https://api.example.com/data', {
  headers: {
    'User-Agent': 'YourApp/1.0'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🚀 快速开始示例

### 示例1：获取天气信息
```javascript
// 使用OpenWeatherMap API
const apiKey = 'your-api-key';
const city = 'Beijing';

fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&lang=zh_cn`)
  .then(response => response.json())
  .then(data => {
    console.log(`${city}当前温度: ${data.main.temp}°C`);
    console.log(`天气状况: ${data.weather[0].description}`);
  });
```

### 示例2：获取随机猫咪图片
```javascript
// 使用Cat Facts API（无需认证）
fetch('https://cataas.com/cat?json=true')
  .then(response => response.json())
  .then(data => {
    const imageUrl = `https://cataas.com${data.url}`;
    console.log('随机猫咪图片:', imageUrl);
  });
```

### 示例3：获取加密货币价格
```javascript
// 使用CoinGecko API（无需认证）
fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,cny')
  .then(response => response.json())
  .then(data => {
    console.log('比特币价格:', data.bitcoin);
    console.log('以太坊价格:', data.ethereum);
  });
```

## 🇨🇳 中国本土API使用

### 百度地图API
```javascript
// 需要在百度地图开放平台申请AK
const ak = 'your-baidu-ak';
const address = '北京市天安门';

fetch(`https://api.map.baidu.com/geocoding/v3/?address=${address}&output=json&ak=${ak}`)
  .then(response => response.json())
  .then(data => {
    if (data.status === 0) {
      console.log('经纬度:', data.result.location);
    }
  });
```

### 和风天气API
```javascript
// 需要在和风天气申请API密钥
const key = 'your-qweather-key';
const location = '101010100'; // 北京的位置ID

fetch(`https://devapi.qweather.com/v7/weather/now?location=${location}&key=${key}`)
  .then(response => response.json())
  .then(data => {
    console.log('当前天气:', data.now);
  });
```

## ⚠️ 注意事项

### 1. API限制
- **请求频率**：注意API的调用频率限制
- **配额限制**：免费API通常有每日/每月调用次数限制
- **地域限制**：某些API可能有地域访问限制

### 2. 错误处理
```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('API调用失败:', error));
```

### 3. 安全考虑
- **API密钥保护**：不要在前端代码中暴露API密钥
- **HTTPS使用**：优先使用支持HTTPS的API
- **数据验证**：对API返回的数据进行验证

## 🛠️ 开发工具推荐

### API测试工具
- **Postman**：功能强大的API测试工具
- **Insomnia**：轻量级的API客户端
- **curl**：命令行HTTP客户端

### 在线工具
- **JSONPlaceholder**：用于测试的假数据API
- **httpbin**：HTTP请求测试服务
- **Webhook.site**：接收和检查HTTP请求

## 📚 进阶学习

### 推荐资源
- [RESTful API设计指南](https://restfulapi.net/)
- [HTTP状态码参考](https://httpstatuses.com/)
- [JSON格式规范](https://www.json.org/)

### 最佳实践
1. **缓存策略**：合理使用缓存减少API调用
2. **错误重试**：实现指数退避重试机制
3. **监控告警**：监控API可用性和响应时间
4. **文档维护**：保持API使用文档的更新

---

如有问题，欢迎提交[Issue](https://github.com/your-repo/public-apis-zh/issues)！
