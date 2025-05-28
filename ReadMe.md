# 🇨🇳 免费公共API大全

[![GitHub stars](https://img.shields.io/github/stars/public-apis-zh/public-apis-zh?style=social)](https://github.com/public-apis-zh/public-apis-zh/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/public-apis-zh/public-apis-zh?style=social)](https://github.com/public-apis-zh/public-apis-zh/network/members)
[![GitHub issues](https://img.shields.io/github/issues/public-apis-zh/public-apis-zh)](https://github.com/public-apis-zh/public-apis-zh/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Public APIs 中文版是一个由社区成员精心维护的公共API集合，包含来自各个领域的大量公共API，您可以在自己的产品中使用这些API。这是一个经过多年社区管理的API宝库。

<br >

## 关于本项目

本项目是 [public-apis](https://github.com/public-apis/public-apis) 的中文本地化版本，旨在为中文开发者提供更好的API资源服务。我们不仅翻译了原有内容，还：

- 🌏 **本地化适配**：针对中文开发者的使用习惯进行优化
- 🔍 **中文搜索**：支持中文关键词搜索和分类
- 🇨🇳 **本土资源**：收录优质的中国本土API服务
- 📚 **详细文档**：提供更详细的中文使用说明
- 🤝 **社区驱动**：欢迎中文开发者社区贡献

<br >

## 如何使用

### 🔍 快速查找
1. 使用页面内搜索（Ctrl+F）查找特定API
2. 通过下方的[分类索引](#分类索引)快速定位
3. 查看每个API的认证方式、HTTPS支持和CORS政策

### 📖 字段说明
| 字段 | 说明 |
|:---|:---|
| **API** | API名称和官方文档链接 |
| **描述** | API功能的简要说明 |
| **认证** | 是否需要API密钥或其他认证方式 |
| **HTTPS** | 是否支持HTTPS安全连接 |
| **CORS** | 是否支持跨域资源共享 |

### 🔐 认证方式说明
- `No` - 无需认证，可直接使用
- `apiKey` - 需要API密钥
- `OAuth` - 需要OAuth认证
- `X-Mashape-Key` - 需要Mashape平台密钥
- `User-Agent` - 需要设置User-Agent头

<br >

## 参与贡献

我们欢迎社区贡献！您可以：

- 🐛 [报告问题](https://github.com/public-apis-zh/public-apis-zh/issues)
- 🔗 [提交新的API](https://github.com/public-apis-zh/public-apis-zh/pulls)
- 📝 [改进翻译](https://github.com/public-apis-zh/public-apis-zh/pulls)
- 💡 [提出建议](https://github.com/public-apis-zh/public-apis-zh/discussions)

详细的贡献指南请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

<br >

## 了解更多

**参与项目**

* [贡献指南](CONTRIBUTING.md)
* [项目API](https://github.com/davemachado/public-api)
* [问题反馈](https://github.com/public-apis-zh/public-apis-zh/issues)
* [拉取请求](https://github.com/public-apis-zh/public-apis-zh/pulls)
* [许可证](LICENSE)

<br >

## 分类索引

* [动物](#动物)
* [动漫](#动漫)
* [反恶意软件](#反恶意软件)
* [艺术与设计](#艺术与设计)
* [身份验证与授权](#身份验证与授权)
* [区块链](#区块链)
* [🇨🇳 中国本土API](#-中国本土api)
* [开发工具](#开发工具)
* [加密货币](#加密货币)
* [健康](#健康)
* [机器学习](#机器学习)
* [音乐](#音乐)
* [新闻](#新闻)
* [编程](#编程)
* [社交](#社交)
* [天气](#天气)

### 动物
API | 描述 | 认证 | HTTPS | CORS
|:---|:---|:---|:---|:---|
| [AdoptAPet](https://www.adoptapet.com/public/apis/pet_list.html) | 帮助宠物被收养的资源 | `apiKey` | Yes | Yes |
| [Axolotl](https://theaxolotlapi.netlify.app/) | 美西螈图片和事实集合 | No | Yes | No |
| [Cat Facts](https://alexwohlbruck.github.io/cat-facts/) | 每日猫咪趣事 | No | Yes | No |
| [Cataas](https://cataas.com/) | 猫咪即服务（猫咪图片和GIF） | No | Yes | No |
| [Cats](https://docs.thecatapi.com/) | 来自Tumblr的猫咪图片 | `apiKey` | Yes | No |
| [Dog Facts](https://dukengn.github.io/Dog-facts-API/) | 随机狗狗趣事 | No | Yes | Yes |
| [Dog Facts](https://kinduff.github.io/dog-api/) | 狗狗的随机趣事 | No | Yes | Yes |
| [Dogs](https://dog.ceo/dog-api/) | 基于斯坦福狗狗数据集 | No | Yes | Yes |
| [eBird](https://documenter.getpostman.com/view/664302/S1ENwy59) | 检索某个地区最近或值得注意的观鸟记录 | `apiKey` | Yes | No |
| [FishWatch](https://www.fishwatch.gov/developers) | 个别鱼类的信息和图片 | No | Yes | Yes |
| [HTTP Cat](https://http.cat/) | 每个HTTP状态对应的猫咪图片 | No | Yes | Yes |
| [HTTP Dog](https://http.dog/) | 每个HTTP响应状态码对应的狗狗图片 | No | Yes | Yes |
| [IUCN](http://apiv3.iucnredlist.org/api/v3/docs) | IUCN濒危物种红色名录 | `apiKey` | No | No |
| [MeowFacts](https://github.com/wh-iterabb-it/meowfacts) | 获取随机猫咪趣事 | No | Yes | No |
| [Movebank](https://github.com/movebank/movebank-api-doc) | 动物的移动和迁徙数据 | No | Yes | Yes |
| [Petfinder](https://www.petfinder.com/developers/) | Petfinder致力于帮助宠物找到家，另一个帮助宠物被收养的资源 | `apiKey` | Yes | Yes |
| [PlaceBear](https://placebear.com/) | 占位符熊图片 | No | Yes | Yes |
| [PlaceDog](https://place.dog) | 占位符狗狗图片 | No | Yes | Yes |
| [PlaceKitten](https://placekitten.com/) | 占位符小猫图片 | No | Yes | Yes |
| [RandomDog](https://random.dog/woof.json) | 随机狗狗图片 | No | Yes | Yes |
| [RandomDuck](https://random-d.uk/api) | 随机鸭子图片 | No | Yes | No |
| [RandomFox](https://randomfox.ca/floof/) | 随机狐狸图片 | No | Yes | No |
| [RescueGroups](https://userguide.rescuegroups.org/display/APIDG/API+Developers+Guide+Home) | 收养 | No | Yes | Unknown |
| [Shibe.Online](http://shibe.online/) | 柴犬、猫咪或鸟类的随机图片 | No | Yes | Yes |
| [The Dog](https://thedogapi.com/) | 关于狗狗的公共服务，在制作精美的新应用、网站或服务时免费使用 | `apiKey` | Yes | No |
| [xeno-canto](https://xeno-canto.org/explore/api) | 鸟类录音 | No | Yes | Unknown |
| [Zoo Animals](https://zoo-animal-api.herokuapp.com/) | 动物园动物的事实和图片 | No | Yes | Yes |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 动漫
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [AniAPI](https://aniapi.com/docs/) | 动漫发现、流媒体和与追踪器同步 | `OAuth` | Yes | Yes |
| [AniDB](https://wiki.anidb.net/HTTP_API_Definition) | 动漫数据库 | `apiKey` | No | Unknown |
| [AniList](https://github.com/AniList/ApiV2-GraphQL-Docs) | 动漫发现和追踪 | `OAuth` | Yes | Unknown |
| [AnimeChan](https://github.com/RocktimSaikia/anime-chan) | 动漫名言（超过10k+） | No | Yes | No |
| [AnimeFacts](https://chandan-02.github.io/anime-facts-rest-api/) | 动漫趣事（超过100+） | No | Yes | Yes |
| [AnimeNewsNetwork](https://www.animenewsnetwork.com/encyclopedia/api.php) | 动漫行业新闻 | No | Yes | Yes |
| [Catboy](https://catboys.com/api) | 猫男孩图片、搞笑GIF等 | No | Yes | Yes |
| [Danbooru Anime](https://danbooru.donmai.us/wiki_pages/help:api) | 数千个动漫艺术家数据库，寻找优秀的动漫艺术 | `apiKey` | Yes | Yes |
| [Jikan](https://jikan.moe) | 非官方MyAnimeList API | No | Yes | Yes |
| [Kitsu](https://kitsu.docs.apiary.io/) | 动漫发现平台 | `OAuth` | Yes | Yes |
| [MangaDex](https://api.mangadx.org/docs.html) | 漫画数据库和社区 | `apiKey` | Yes | Unknown |
| [Mangapi](https://rapidapi.com/pierre.carcellermeunier/api/mangapi3/) | 将漫画页面从一种语言翻译成另一种语言 | `apiKey` | Yes | Unknown |
| [MyAnimeList](https://myanimelist.net/clubs.php?cid=13727) | 动漫和漫画数据库及社区 | `OAuth` | Yes | Unknown |
| [NekosBest](https://docs.nekos.best) | 猫娘图片和动漫角色扮演GIF | No | Yes | Yes |
| [Shikimori](https://shikimori.one/api/doc) | 动漫发现、追踪、论坛、评分 | `OAuth` | Yes | Unknown |
| [Studio Ghibli](https://ghibliapi.herokuapp.com) | 吉卜力工作室电影资源 | No | Yes | Yes |
| [Trace Moe](https://soruly.github.io/trace.moe-api/#/) | 从截图中获取动漫确切场景的有用工具 | No | Yes | No |
| [Waifu.im](https://waifu.im/docs) | 从超过4000张图片和多个标签的档案中获取老婆图片 | No | Yes | Yes |
| [Waifu.pics](https://waifu.pics/docs) | 动漫图片分享平台 | No | Yes | No |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 反恶意软件
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [AbuseIPDB](https://docs.abuseipdb.com/) | IP/域名/URL声誉 | `apiKey` | Yes | Unknown |
| [AlienVault Open Threat Exchange (OTX)](https://otx.alienvault.com/api) | IP/域名/URL声誉 | `apiKey` | Yes | Unknown |
| [CAPEsandbox](https://capev2.readthedocs.io/en/latest/usage/api.html) | 恶意软件执行和分析 | `apiKey` | Yes | Unknown |
| [Google Safe Browsing](https://developers.google.com/safe-browsing/) | Google链接/域名标记 | `apiKey` | Yes | Unknown |
| [MalDatabase](https://maldatabase.com/api-doc.html) | 提供恶意软件数据集和威胁情报源 | `apiKey` | Yes | Unknown |
| [MalShare](https://malshare.com/doc.php) | 恶意软件档案/文件来源 | `apiKey` | Yes | No |
| [MalwareBazaar](https://bazaar.abuse.ch/api/) | 收集和分享恶意软件样本 | `apiKey` | Yes | Unknown |
| [Metacert](https://metacert.com/) | Metacert链接标记 | `apiKey` | Yes | Unknown |
| [NoPhishy](https://rapidapi.com/Amiichu/api/exerra-phishing-check/) | 检查链接是否为已知钓鱼尝试 | `apiKey` | Yes | Yes |
| [Phisherman](https://phisherman.gg/) | IP/域名/URL声誉 | `apiKey` | Yes | Unknown |
| [Scanii](https://docs.scanii.com/) | 可以扫描提交的文档/文件是否存在威胁的简单REST API | `apiKey` | Yes | Yes |
| [URLhaus](https://urlhaus-api.abuse.ch/) | 批量查询和下载恶意软件样本 | No | Yes | Yes |
| [URLScan.io](https://urlscan.io/about-api/) | 扫描和分析URL | `apiKey` | Yes | Unknown |
| [VirusTotal](https://www.virustotal.com/en/documentation/public-api/) | VirusTotal文件/URL分析 | `apiKey` | Yes | Unknown |
| [Web of Trust](https://support.mywot.com/hc/en-us/sections/360004477734-API-) | IP/域名/URL声誉 | `apiKey` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 艺术与设计
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [Améthyste](https://api.amethyste.moe/) | 为Discord用户生成图片 | `apiKey` | Yes | Unknown |
| [Art Institute of Chicago](https://api.artic.edu/docs/) | 艺术 | No | Yes | Yes |
| [Colormind](http://colormind.io/api-access/) | 配色方案生成器 | No | No | Unknown |
| [ColourLovers](http://www.colourlovers.com/api) | 获取各种图案、调色板和图片 | No | No | Unknown |
| [Cooper Hewitt](https://collection.cooperhewitt.org/api) | 史密森尼设计博物馆 | `apiKey` | Yes | Unknown |
| [Dribbble](https://developer.dribbble.com) | 发现世界顶级设计师和创意人员 | `OAuth` | Yes | Unknown |
| [EmojiHub](https://github.com/cheatsnake/emojihub) | 按类别和组获取表情符号 | No | Yes | Yes |
| [Europeana](https://pro.europeana.eu/resources/apis/search) | 欧洲博物馆和画廊内容 | `apiKey` | Yes | Unknown |
| [Harvard Art Museums](https://github.com/harvardartmuseums/api-docs) | 艺术 | `apiKey` | No | Unknown |
| [Icon Horse](https://icon.horse) | 任何网站的图标，带有后备选项 | No | Yes | Yes |
| [Iconfinder](https://developer.iconfinder.com) | 图标 | `apiKey` | Yes | Unknown |
| [Icons8](https://img.icons8.com/) | 图标（在页面中查找"搜索图标"超链接） | No | Yes | Unknown |
| [Lordicon](https://lordicon.com/) | 带有预制动画的图标 | No | Yes | Yes |
| [Metropolitan Museum of Art](https://metmuseum.github.io/) | 大都会艺术博物馆 | No | Yes | No |
| [Noun Project](http://api.thenounproject.com/index.html) | 图标 | `OAuth` | No | Unknown |
| [PHP-Noise](https://php-noise.com/) | 噪声背景图片生成器 | No | Yes | Yes |
| [Pixel Encounter](https://pixelencounter.com/api) | SVG图标生成器 | No | Yes | No |
| [Rijksmuseum](https://data.rijksmuseum.nl/object-metadata/api/) | 荷兰国立博物馆数据 | `apiKey` | Yes | Unknown |
| [Word Cloud](https://wordcloudapi.com/) | 轻松创建词云 | `apiKey` | Yes | Unknown |
| [xColors](https://x-colors.herokuapp.com/) | 生成和转换颜色 | No | Yes | Yes |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 身份验证与授权
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [Auth0](https://auth0.com) | 易于实现、适应性强的身份验证和授权平台 | `apiKey` | Yes | Yes |
| [GetOTP](https://otp.dev/en/docs/) | 快速实现OTP流程 | `apiKey` | Yes | No |
| [Micro User Service](https://m3o.com/user) | 用户管理和身份验证 | `apiKey` | Yes | No |
| [MojoAuth](https://mojoauth.com) | 安全现代的无密码身份验证平台 | `apiKey` | Yes | Yes |
| [SAWO Labs](https://sawolabs.com) | 通过在应用中集成无密码身份验证来简化登录并改善用户体验 | `apiKey` | Yes | Yes |
| [Stytch](https://stytch.com/) | 现代应用的用户基础设施 | `apiKey` | Yes | No |
| [Warrant](https://warrant.dev/) | 授权和访问控制API | `apiKey` | Yes | Yes |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 区块链
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [Bitquery](https://graphql.bitquery.io/ide) | 链上GraphQL API和DEX API | `apiKey` | Yes | Yes |
| [Chainlink](https://chain.link/developer-resources) | 使用Chainlink构建混合智能合约 | No | Yes | Unknown |
| [Chainpoint](https://tierion.com/chainpoint/) | Chainpoint是将数据锚定到比特币区块链的全球网络 | No | Yes | Unknown |
| [Covalent](https://www.covalenthq.com/docs/api/) | 多区块链数据聚合平台 | `apiKey` | Yes | Unknown |
| [Etherscan](https://etherscan.io/apis) | 以太坊浏览器API | `apiKey` | Yes | Yes |
| [Helium](https://docs.helium.com/api/blockchain/introduction/) | Helium是一个由热点组成的全球分布式网络，创建公共的远程无线覆盖 | No | Yes | Unknown |
| [Nownodes](https://nownodes.io/) | 通过API提供高质量连接的区块链即服务解决方案 | `apiKey` | Yes | Unknown |
| [Steem](https://developers.steem.io/) | 基于区块链的博客和社交媒体网站 | No | No | No |
| [The Graph](https://thegraph.com) | 使用GraphQL查询以太坊等网络的索引协议 | `apiKey` | Yes | Unknown |
| [Walltime](https://walltime.info/api.html) | 检索Walltime的市场信息 | No | Yes | Unknown |
| [Watchdata](https://docs.watchdata.io) | 提供对以太坊区块链的简单可靠的API访问 | `apiKey` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 开发工具
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [24 Pull Requests](https://24pullrequests.com/api) | 促进12月开源协作的项目 | No | Yes | Yes |
| [Agify.io](https://agify.io) | 从名字估算年龄 | No | Yes | Yes |
| [API Grátis](https://apigratis.com.br/) | 多种服务和公共API | No | Yes | Unknown |
| [Screenshot](https://www.abstractapi.com/website-screenshot-api) | 以编程方式截取任何网站的网页截图 | `apiKey` | Yes | Yes |
| [ApicAgent](https://www.apicagent.com) | 从用户代理字符串中提取设备详细信息 | No | Yes | Yes |
| [ApiFlash](https://apiflash.com/) | 基于Chrome的开发者截图API | `apiKey` | Yes | Unknown |
| [apilayer userstack](https://userstack.com/) | 安全的用户代理字符串查找JSON API | `OAuth` | Yes | Unknown |
| [APIs.guru](https://apis.guru/api-doc/) | Web API的维基百科，公共API的OpenAPI/Swagger规范 | No | Yes | Unknown |
| [Azure DevOps](https://docs.microsoft.com/en-us/rest/api/azure/devops) | Azure DevOps REST API请求/响应对的基本组件 | `apiKey` | Yes | Unknown |
| [Base](https://www.base-api.io/) | 快速构建后端 | `apiKey` | Yes | Yes |
| [Beeceptor](https://beeceptor.com/) | 在几秒钟内构建模拟Rest API端点 | No | Yes | Yes |
| [Bitbucket](https://developer.atlassian.com/bitbucket/api/2/reference/) | Bitbucket API | `OAuth` | Yes | Unknown |
| [Blague.xyz](https://blague.xyz/) | 最大的法语笑话API | `apiKey` | Yes | Yes |
| [Blitapp](https://blitapp.com/api/) | 安排网页截图并同步到您的云端 | `apiKey` | Yes | Unknown |
| [Blynk-Cloud](https://blynkapi.docs.apiary.io/#) | 从Blynk物联网云控制物联网设备 | `apiKey` | No | Unknown |
| [Bored](https://www.boredapi.com/) | 寻找随机活动来对抗无聊 | No | Yes | Unknown |
| [Brainshop.ai](https://brainshop.ai/) | 制作免费的AI大脑 | `apiKey` | Yes | Yes |
| [Browshot](https://browshot.com/api/documentation) | 轻松制作任何屏幕尺寸、任何设备的网页截图 | `apiKey` | Yes | Yes |
| [CDNJS](https://api.cdnjs.com/libraries/jquery) | CDNJS上的库信息 | No | Yes | Unknown |
| [Changelogs.md](https://changelogs.md) | 来自开源项目的结构化变更日志元数据 | No | Yes | Unknown |
| [Ciprand](https://github.com/polarspetroll/ciprand) | 安全随机字符串生成器 | No | Yes | No |
| [Cloudflare Trace](https://github.com/fawazahmed0/cloudflare-trace-api) | 获取IP地址、时间戳、用户代理、国家代码、IATA、HTTP版本、TLS/SSL版本等 | No | Yes | Yes |
| [Codex](https://github.com/Jaagrav/CodeX) | 各种语言的在线编译器 | No | Yes | Unknown |
| [Contentful Images](https://www.contentful.com/developers/docs/references/images-api/) | 用于检索和应用图像转换 | `apiKey` | Yes | Yes |
| [CORS Proxy](https://github.com/burhanuday/cors-proxy) | 使用此代理作为中间人来解决可怕的CORS错误 | No | Yes | Yes |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 天气
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [7Timer!](http://www.7timer.info/doc.php?lang=en) | 天气预报API，数值天气预报 | No | No | Unknown |
| [AccuWeather](https://developer.accuweather.com/apis) | 天气和预报API | `apiKey` | Yes | Unknown |
| [Aeris Weather](https://www.aerisweather.com/support/docs/api/) | 高级天气API | `apiKey` | Yes | Unknown |
| [apilayer weatherstack](https://weatherstack.com/) | 实时天气API，支持全球任何位置 | `apiKey` | Yes | Unknown |
| [APIXU](https://www.apixu.com/doc.aspx) | 天气API | `apiKey` | Yes | Unknown |
| [AviationWeather](https://www.aviationweather.gov/dataserver) | NOAA航空天气中心API | No | Yes | Unknown |
| [ColorfulClouds](https://open.caiyunapp.com/ColorfulClouds_Weather_API) | 彩云天气API，支持全球天气查询 | `apiKey` | Yes | Yes |
| [Dark Sky](https://darksky.net/dev) | 天气API（已停止新注册） | `apiKey` | Yes | Unknown |
| [MetaWeather](https://www.metaweather.com/api/) | 天气API | No | Yes | No |
| [Meteorologisk Institutt](https://api.met.no/weatherapi/documentation) | 挪威气象研究所的天气API | `User-Agent` | Yes | Unknown |
| [NOAA Climate Data](https://www.ncdc.noaa.gov/cdo-web/) | NOAA气候数据在线 | `apiKey` | Yes | Unknown |
| [ODWeather](http://api.oceandrivers.com/static/docs.html) | 天气和海洋学数据 | No | No | Unknown |
| [OpenUV](https://www.openuv.io) | 实时紫外线指数预报 | `apiKey` | Yes | Unknown |
| [OpenWeatherMap](https://openweathermap.org/api) | 天气API | `apiKey` | Yes | Unknown |
| [Storm Glass](https://stormglass.io/) | 全球天气、海洋和环境数据 | `apiKey` | Yes | Yes |
| [Sunrise and Sunset](https://sunrise-sunset.org/api) | 日出日落时间API | No | Yes | Yes |
| [Visual Crossing](https://www.visualcrossing.com/weather-api) | 全球历史和天气预报数据 | `apiKey` | Yes | Yes |
| [WeatherAPI](https://www.weatherapi.com/) | 天气API以及天文学和地理位置API | `apiKey` | Yes | Yes |
| [Weatherbit](https://www.weatherbit.io/api) | 天气 | `apiKey` | Yes | Unknown |
| [Yandex.Weather](https://yandex.com/dev/weather/) | 评估特定位置的天气状况 | `apiKey` | Yes | No |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 加密货币
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [0x](https://0x.org/api) | 查询各种流动性池的代币和池统计数据的API | No | Yes | Yes |
| [1inch](https://1inch.io/api/) | 查询去中心化交易所的API | No | Yes | Unknown |
| [Alchemy Ethereum](https://docs.alchemy.com/alchemy/) | 以太坊节点即服务提供商 | `apiKey` | Yes | Yes |
| [apilayer coinlayer](https://coinlayer.com) | 实时加密货币汇率 | `apiKey` | Yes | Unknown |
| [Binance](https://github.com/binance/binance-spot-api-docs) | 基于中国的加密货币交易所 | `apiKey` | Yes | Unknown |
| [Bitcambio](https://nova.bitcambio.com.br/api/v3/docs#a-public) | 获取交易所中所有交易资产的列表 | No | Yes | Unknown |
| [BitcoinAverage](https://apiv2.bitcoinaverage.com/) | 区块链行业的数字资产价格数据 | `apiKey` | Yes | Unknown |
| [BitcoinCharts](https://bitcoincharts.com/about/exchanges/) | 与比特币网络相关的金融和技术数据 | No | Yes | Unknown |
| [Bitfinex](https://docs.bitfinex.com/docs) | 加密货币交易平台 | `apiKey` | Yes | Unknown |
| [Bitmex](https://www.bitmex.com/app/apiOverview) | 基于香港的实时加密货币衍生品交易平台 | `apiKey` | Yes | Unknown |
| [Bittrex](https://bittrex.github.io/api/v3) | 下一代加密交易平台 | `apiKey` | Yes | Unknown |
| [Block](https://block.io/docs/basic) | 比特币支付、钱包和交易数据 | `apiKey` | Yes | Unknown |
| [Blockchain](https://www.blockchain.com/api) | 比特币支付、钱包和交易数据 | `apiKey` | Yes | Unknown |
| [blockfrost Cardano](https://blockfrost.io/) | 与Cardano主网和多个测试网的交互 | `apiKey` | Yes | Unknown |
| [Brave NewCoin](https://bravenewcoin.com/developers) | 来自200多个交易所的实时和历史加密数据 | `apiKey` | Yes | Unknown |
| [BtcTurk](https://docs.btcturk.com/) | 实时加密货币数据、图表和允许买卖的API | `apiKey` | Yes | Yes |
| [Bybit](https://bybit-exchange.github.io/docs/linear/#t-introduction) | 加密货币数据源和算法交易 | `apiKey` | Yes | Unknown |
| [CoinAPI](https://docs.coinapi.io/) | 所有货币交易所集成在单一API下 | `apiKey` | Yes | No |
| [Coinbase](https://developers.coinbase.com) | 比特币、比特币现金、莱特币和以太坊价格 | `apiKey` | Yes | Unknown |
| [Coinbase Pro](https://docs.pro.coinbase.com/#api) | 加密货币交易平台 | `apiKey` | Yes | Unknown |
| [CoinCap](https://docs.coincap.io/) | 通过RESTful API获取实时加密货币价格 | No | Yes | Unknown |
| [CoinDCX](https://docs.coindcx.com/) | 加密货币交易平台 | `apiKey` | Yes | Unknown |
| [CoinDesk](https://old.coindesk.com/coindesk-api/) | CoinDesk的比特币价格指数（BPI）多种货币 | No | Yes | Unknown |
| [CoinGecko](http://www.coingecko.com/api) | 加密货币价格、市场和开发者/社交数据 | No | Yes | Yes |
| [Coinigy](https://coinigy.docs.apiary.io) | 直接与Coinigy账户和交易所交互 | `apiKey` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 🇨🇳 中国本土API
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [APISpace](https://www.apispace.com/) | 一站式API服务平台 | `apiKey` | Yes | Yes |
| [阿里云API](https://help.aliyun.com/product/29991.html) | 阿里云各种服务API | `apiKey` | Yes | Yes |
| [百度AI开放平台](https://ai.baidu.com/) | 百度AI服务API | `apiKey` | Yes | Yes |
| [百度地图API](https://lbsyun.baidu.com/index.php?title=webapi) | 百度地图Web服务API | `apiKey` | Yes | Yes |
| [彩云天气API](https://open.caiyunapp.com/ColorfulClouds_Weather_API) | 精准的天气预报API | `apiKey` | Yes | Yes |
| [高德地图API](https://lbs.amap.com/api/) | 高德地图Web服务API | `apiKey` | Yes | Yes |
| [和风天气API](https://dev.qweather.com/) | 全球天气数据服务 | `apiKey` | Yes | Yes |
| [京东万象API](https://wx.jdcloud.com/) | 京东万象数据服务API | `apiKey` | Yes | Unknown |
| [聚合数据API](https://www.juhe.cn/) | 提供各种生活服务数据API | `apiKey` | Yes | Unknown |
| [QQ音乐API](https://y.qq.com/) | QQ音乐相关API | No | Yes | Unknown |
| [腾讯AI开放平台](https://ai.qq.com/) | 腾讯AI服务API | `apiKey` | Yes | Yes |
| [腾讯地图API](https://lbs.qq.com/webApi/javascriptGL/glGuide/glOverview) | 腾讯地图Web服务API | `apiKey` | Yes | Yes |
| [腾讯云API](https://cloud.tencent.com/document/api) | 腾讯云各种服务API | `apiKey` | Yes | Yes |
| [天行数据API](https://www.tianapi.com/) | 免费数据接口API | `apiKey` | Yes | Unknown |
| [微博API](https://open.weibo.com/wiki/API) | 新浪微博开放平台API | `OAuth` | Yes | Unknown |
| [微信公众平台API](https://developers.weixin.qq.com/doc/) | 微信公众号开发API | `OAuth` | Yes | Unknown |
| [网易云音乐API](https://neteasecloudmusicapi.vercel.app/) | 网易云音乐非官方API | No | Yes | Yes |
| [讯飞开放平台](https://www.xfyun.cn/) | 科大讯飞AI服务API | `apiKey` | Yes | Yes |
| [易源数据API](https://www.showapi.com/) | 各种数据服务API | `apiKey` | Yes | Unknown |
| [支付宝开放平台](https://opendocs.alipay.com/apis) | 支付宝各种服务API | `OAuth` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 新闻
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [apilayer mediastack](https://mediastack.com/) | 免费、简单的实时新闻和博客文章REST API | `apiKey` | Yes | Unknown |
| [Associated Press](https://developer.ap.org/) | 从美联社搜索新闻和元数据 | `apiKey` | Yes | Unknown |
| [Chronicling America](http://chroniclingamerica.loc.gov/about/api/) | 提供对国会图书馆数百万页历史美国报纸的访问 | No | No | Unknown |
| [Currents](https://currentsapi.services/) | 在各种新闻来源、博客和论坛中发布的最新新闻 | `apiKey` | Yes | Yes |
| [Feedbin](https://github.com/feedbin/feedbin-api) | RSS阅读器 | `OAuth` | Yes | Unknown |
| [GNews](https://gnews.io/) | 搜索全球新闻 | `apiKey` | Yes | Yes |
| [Inshorts](https://github.com/cyberboysumanjay/Inshorts-News-API) | 提供来自inshorts的新闻 | No | Yes | Unknown |
| [MarketAux](https://www.marketaux.com/) | 实时金融新闻和市场数据 | `apiKey` | Yes | Yes |
| [New York Times](https://developer.nytimes.com/) | 《纽约时报》新闻 | `apiKey` | Yes | Unknown |
| [News](https://newsapi.org/) | 来自全球70,000多个新闻来源的头条新闻和文章 | `apiKey` | Yes | Unknown |
| [NPR One](http://dev.npr.org/api/) | NPR One收听体验 | `OAuth` | Yes | Unknown |
| [Spaceflight News](https://spaceflightnewsapi.net) | 航天新闻 | No | Yes | Yes |
| [The Guardian](http://open-platform.theguardian.com/) | 访问《卫报》的所有内容 | `apiKey` | Yes | Unknown |
| [The Old Reader](https://github.com/theoldreader/api) | RSS阅读器 | `apiKey` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 社交
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [4chan](https://github.com/4chan/4chan-API) | 简单的只读API，用于检索线程和帖子 | No | Yes | Yes |
| [Buffer](https://buffer.com/developers/api) | 访问用户的待发布和已发布更新 | `OAuth` | Yes | Unknown |
| [Cisco Spark](https://developer.ciscospark.com) | 团队协作软件 | `OAuth` | Yes | Unknown |
| [Discord](https://discord.com/developers/docs/intro) | 为您的游戏制作机器人 | `OAuth` | Yes | Unknown |
| [Disqus](https://disqus.com/api/docs/auth/) | 与Disqus数据通信 | `OAuth` | Yes | Unknown |
| [Facebook](https://developers.facebook.com/) | Facebook登录、分享、评论、广告等 | `OAuth` | Yes | Unknown |
| [Foursquare](https://developer.foursquare.com/) | 与Foursquare用户和商家互动 | `OAuth` | Yes | Unknown |
| [Fuck Off as a Service](https://www.foaas.com) | 请求各种形式的"滚蛋" | No | Yes | Unknown |
| [Full Contact](https://www.fullcontact.com/developer/docs/) | 获取社交媒体资料和联系信息 | `OAuth` | Yes | Unknown |
| [HackerNews](https://github.com/HackerNews/API) | 社交新闻网络 | No | Yes | Unknown |
| [Instagram](https://www.instagram.com/developer/) | Instagram登录、分享照片、社交互动 | `OAuth` | Yes | Unknown |
| [LinkedIn](https://developer.linkedin.com/docs/rest-api) | 世界最大的专业网络 | `OAuth` | Yes | Unknown |
| [Meetup.com](https://www.meetup.com/meetup_api/) | 数据关于聚会组 | `apiKey` | Yes | Unknown |
| [Pinterest](https://developers.pinterest.com/) | 世界的想法目录 | `OAuth` | Yes | Unknown |
| [Reddit](https://www.reddit.com/dev/api) | 主页互联网 | `OAuth` | Yes | Unknown |
| [Slack](https://api.slack.com/) | 团队协作 | `OAuth` | Yes | Unknown |
| [Telegram Bot](https://core.telegram.org/bots/api) | 简化Telegram机器人的使用 | `apiKey` | Yes | Unknown |
| [Tumblr](https://www.tumblr.com/docs/en/api/v2) | 阅读和写入Tumblr数据 | `OAuth` | Yes | Unknown |
| [Twitch](https://dev.twitch.tv/docs) | 游戏直播API | `OAuth` | Yes | Unknown |
| [Twitter](https://developer.twitter.com/en/docs) | 阅读和写入Twitter数据 | `OAuth` | Yes | No |
| [vk](https://vk.com/dev/sites) | 读取和写入vk.com数据 | `OAuth` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 机器学习
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [AI For People](https://aiforpeople.org) | AI服务和模型 | No | Yes | Unknown |
| [Clarifai](https://docs.clarifai.com/api-guide/api-overview) | 计算机视觉 | `apiKey` | Yes | Unknown |
| [Deepcode](https://www.deepcode.ai) | AI代码审查 | No | Yes | Unknown |
| [Dialogflow](https://cloud.google.com/dialogflow/docs/) | 自然语言理解 | `apiKey` | Yes | Unknown |
| [EXUDE-API](http://uttesh.com/exude-api/) | 信息提取 | No | Yes | Yes |
| [Keen IO](https://keen.io/) | 数据分析 | `apiKey` | Yes | Unknown |
| [Machinetutors](https://www.machinetutors.com/portfolio/MT_api.html) | AI和机器学习 | `apiKey` | Yes | Yes |
| [MessengerX.io](https://messengerx.rtfd.io) | 聊天机器人平台 | `apiKey` | Yes | Unknown |
| [NLP Cloud](https://nlpcloud.io) | NLP API使用spaCy和transformers | `apiKey` | Yes | Unknown |
| [OpenAI](https://openai.com/api/) | AI模型和服务 | `apiKey` | Yes | Unknown |
| [Perspective](https://perspectiveapi.com) | 评论毒性检测 | `apiKey` | Yes | Unknown |
| [Roboflow](https://docs.roboflow.com/) | 计算机视觉 | `apiKey` | Yes | Yes |
| [SkyBiometry](https://skybiometry.com/documentation/) | 人脸检测和识别 | `apiKey` | Yes | Unknown |
| [Wit.ai](https://wit.ai/) | 自然语言处理 | `OAuth` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 音乐
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [7digital](https://docs.7digital.com/reference) | 音乐商店 | `OAuth` | Yes | Unknown |
| [Audiomack](https://www.audiomack.com/data-api/docs) | 音乐流媒体 | `OAuth` | Yes | Unknown |
| [Bandsintown](https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.0) | 音乐活动 | No | Yes | Unknown |
| [Deezer](https://developers.deezer.com/api) | 音乐 | `OAuth` | Yes | Unknown |
| [Discogs](https://www.discogs.com/developers/) | 音乐 | `OAuth` | Yes | Unknown |
| [Genius](https://docs.genius.com/) | 歌词和音乐注释 | `OAuth` | Yes | Unknown |
| [Jamendo](https://developer.jamendo.com/v3.0/docs) | 音乐 | `OAuth` | Yes | Unknown |
| [Last.fm](https://www.last.fm/api) | 音乐 | `apiKey` | Yes | Unknown |
| [ListenNotes](https://www.listennotes.com/api/docs/) | 播客搜索 | `apiKey` | Yes | Yes |
| [Lyrics.ovh](https://lyricsovh.docs.apiary.io/) | 简单API获取歌词 | No | Yes | Unknown |
| [Mixcloud](https://www.mixcloud.com/developers/) | 音乐 | `OAuth` | Yes | Yes |
| [MusicBrainz](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2) | 音乐元数据 | No | Yes | Unknown |
| [Musixmatch](https://developer.musixmatch.com/) | 音乐 | `apiKey` | Yes | Unknown |
| [Napster](https://developer.napster.com/api/v2.2) | 音乐 | `apiKey` | Yes | Yes |
| [Openwhyd](https://openwhyd.github.io/openwhyd/API) | 下载来自各种流媒体服务的曲目 | No | Yes | No |
| [Podcast Index](https://podcastindex-org.github.io/docs-api/) | 播客数据库 | `apiKey` | Yes | Unknown |
| [Radio Browser](https://api.radio-browser.info/) | 电台目录 | No | Yes | Yes |
| [Songkick](https://www.songkick.com/developer/) | 音乐活动 | `OAuth` | Yes | Unknown |
| [Songlink / Odesli](https://www.notion.so/API-d0ebe08a5e304a55928405eb682f6741) | 获取音乐平台链接 | `apiKey` | Yes | Yes |
| [SoundCloud](https://developers.soundcloud.com/docs/api/guide) | 允许用户上传和分享声音 | `OAuth` | Yes | Unknown |
| [Spotify](https://developer.spotify.com/web-api/) | 查看Spotify音乐目录、管理用户播放列表等 | `OAuth` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 编程
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [Codeforces](https://codeforces.com/apiHelp) | 获取比赛、问题、提交等信息 | `apiKey` | Yes | Unknown |
| [CodePen](https://blog.codepen.io/documentation/api/) | 提供对CodePen的编程访问 | `apiKey` | Yes | Unknown |
| [Hackerearth](https://www.hackerearth.com/docs/wiki/developers/v4/) | 为开发者提供编程挑战 | `apiKey` | Yes | Unknown |
| [HackerRank](https://www.hackerrank.com/api/docs) | 编程挑战 | `apiKey` | Yes | Unknown |
| [Judge0](https://api.judge0.com/) | 编译和运行源代码 | `apiKey` | Yes | Unknown |
| [KONTESTS](https://kontests.net/api) | 获取来自各种编程平台的比赛信息 | No | Yes | Unknown |
| [Mintlify](https://docs.mintlify.com) | 为代码生成文档 | `apiKey` | Yes | Yes |
| [ReqRes](https://reqres.in/) | 托管的REST-API，可用于测试HTTP请求 | No | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

### 健康
API | 描述 | 认证 | HTTPS | CORS |
|:---|:---|:---|:---|:---|
| [CMS.gov](https://data.cms.gov/provider-data/) | 访问CMS数据集 | `apiKey` | Yes | Unknown |
| [Coronavirus](https://pipedream.com/@pravin/http-api-for-latest-wuhan-coronavirus-data-2019-ncov-p_G6CLVM/readme) | HTTP API获取最新的武汉冠状病毒数据 | No | Yes | Unknown |
| [Covid-19](https://covid19api.com/) | Covid 19传播、恢复和死亡数据 | No | Yes | Yes |
| [Covid-19 Government Response](https://covidtracker.bsg.ox.ac.uk) | 政府对Covid-19的响应数据 | No | Yes | Yes |
| [Diabetes](http://predictbgl.com/api/) | 糖尿病预测 | No | Yes | Unknown |
| [Flutrack](https://flutrack.org/) | 流感样疾病监测 | No | No | Unknown |
| [Healthcare.gov](https://www.healthcare.gov/developers/) | 医疗保健信息 | No | Yes | Unknown |
| [Lexigram](https://docs.lexigram.io/) | NLP API用于医疗决策支持 | `apiKey` | Yes | Unknown |
| [Makeup](http://makeup-api.herokuapp.com/) | 化妆品信息 | No | No | Unknown |
| [Medicare](https://data.medicare.gov/developers) | 访问大量的医疗保险数据集 | No | Yes | Unknown |
| [NPPES](https://npiregistry.cms.hhs.gov/registry/help-api) | 国家提供商标识符数据库API | No | Yes | Unknown |
| [Nutritionix](https://developer.nutritionix.com/) | 世界上最大的营养数据库 | `apiKey` | Yes | Unknown |
| [Open Disease](https://disease.sh/) | 疾病相关统计数据 | No | Yes | Yes |
| [OpenFDA](https://open.fda.gov/apis/) | 公共FDA数据关于药物、设备和食品 | `apiKey` | Yes | Unknown |
| [Orion Health](https://developer.orionhealth.io/) | 医疗平台，可以访问大量的医疗数据 | `OAuth` | Yes | Unknown |

**[⬆ 返回索引](#分类索引)**
<br >
<br >

## 许可证

[MIT](LICENSE) © 2024 public-apis-zh

---

## 致谢

感谢原始的 [public-apis](https://github.com/public-apis/public-apis) 项目提供了优秀的基础。

本项目由中文开发者社区维护，欢迎大家贡献！

---

**⭐ 如果这个项目对您有帮助，请给我们一个星标！**