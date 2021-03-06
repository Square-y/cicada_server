[TOC]

文章喜欢信息存储mysql数据库

| 字段                 | 属性   | 是否必填 | 备注           |
| -------------------- | ------ | -------- | -------------- |
| id                   | int    | 是       | 序号           |
| liked_article_id     | int    | 是       | 被喜欢的文章   |
| like_article_user_id | int    | 是       | 喜欢文章的用户 |
| like_status          | int    | 是       | 点赞状态       |
| create_time          | bigint | 是       | 创建时间       |

文章点赞信息存储redis数据库



文章存到mysql数据库。表名article

| 字段        | 属性       | 是否必填 | 备注         |
| ----------- | ---------- | -------- | ------------ |
| id          | int        | 否       | 序号，主键   |
| title       | varchar    | 否       | 标题         |
| contents    | txt        | 否       | 文章内容     |
| introduce   | char（50） | 否       | 文章简介     |
| create_time | char（15） | 是       | 创建时间     |
| update_time | char（15） | 是       | 更新时间     |
| author_id   | int        | 是       | 作者         |
| categories  | varchar    | 否       | 文章类别     |
| private     | char       | 是       | 私有或者公开 |

已收藏的文章的数据库

| 字段                     | 属性 | 是否必填 | 备注               |
| ------------------------ | ---- | -------- | ------------------ |
| id                       | int  | 是       | 序号               |
| favorited_article_id     | int  | 是       | 被收藏的文章id     |
| favorite_article_user_id | int  | 是       | 收藏文章的用户的id |
| favorite_status          | int  | 是       | 收藏的状态         |
| create_time              | int  | 是       | 收藏时间           |

点赞信息存储数据库

| 字段                   | 属性 | 是否必填 | 备注               |
| ---------------------- | ---- | -------- | ------------------ |
| id                     | int  | 是       | 序号               |
| praised_article_id     | int  | 是       | 被收藏的文章id     |
| praise_article_user_id | int  | 是       | 收藏文章的用户的id |
| praise_status          | int  | 是       | 收藏的状态         |
| create_time            | int  | 是       | 收藏时间           |

### 一、展示推荐文章列表

```python
URL:http://127.0.0.1:5000/articles/commend
```

#### 1、请求方式

```python
GET
```

#### 2、请求格式

```python
无
```

#### 3、响应格式

```python
json
{	
    retCode:'000'
    reMsg:'获取推荐文章成功'
    info:[
        id:1,
        "title":"",
        "content":"",
        highlight:'',
        author:'',
        "avatar":"",
        create_time:'',
        "_image":"",
       	like:0,
        liked:1
    ],
    [
        id:12
        introduce:'',
        author_id:'',
        create_time:''
        like:0,
        liked:0
    ]
}
```

#### 4、错误码

```python

```



### 二、展示热点文章列表

```python
URL:http://127.0.0.1/articles/hot
```

#### 1、请求方式

```python
GET
```

#### 2、请求格式

```python
无
```

#### 3、响应格式

```python
json
{	
    retCode:'000'
    reMsg:'获取热点文章成功'
    articles:[
        id:1,
        introduce:'',
        author_id:'',
        create_time:'',
       	like:0,
        liked:1
    ],
    [
        id:12
        introduce:'',
        author_id:'',
        create_time:''
        like:0,
        liked:0
    ]
}
```

### 三、展示收藏文章的列表

```python
URL:http://127.0.0.1/articles/favorites
```

#### 1、请求方式

```python
GET
```

#### 2、请求格式

```python
无
```

#### 3、响应格式

```python
json
{	
    retCode:'000'
    reMsg:'获取热点文章成功'
    articles:[
        id:1,
        introduce:'',
        author_id:'',
        create_time:'',
       	like:0,
        liked:1
    ],
    [
        id:12
        introduce:'',
        author_id:'',
        create_time:''
        like:0,
        liked:0
    ]
}
```

### 四、展示文章详情

```python
URL:http://127.0.0.1/articles/id
```

#### 1、请求方式

```python
GET
```

#### 2、请求格式

```python
查询字符串
```

#### 3、响应格式

```python
json
{	
    "retCode":'000'
    "reMsg":'获取热点文章成功'
    "article":{
        "id":1,
        "content":'',
        "author":'',
        "update_time":'',
        # 当前文章的喜欢状态,0未喜欢，1为已喜欢
       	"like_status": 0,
        # 喜欢的数量
        "liked":1,
        "img":''
    }
}
```

### 五、发表文章

```python
URL:http://127.0.0.1:5000/users/6060366bc4435980de3010b8/article
```

#### 1、请求方式

```python
POST
```

#### 2、请求格式

```python
{
    'title':'',
    'content':'',
    'author_id':'',
    'categories':'技术',
    'public': 1,
    "status":1,
    "create_time":"",
    "update_time":""
    "user_id":""
}
```

3、响应格式

```python
{
    "retCode":"000",
    "retMsg":"保存文章成功"
}
```



### 六、修改文章

```python
URL:http://127.0.0.1/article/6064183735a16f811237f348
```

#### 1、请求方式

```python
PUT
```

#### 2、请求格式

```python
{
    "_id":""
    'title':'',
    'contents':'',
    "introduce":"",
    'update_time':'',
    'author_id':'',
    'categories':'技术',
    'private': '公开'
    
}
```

#### 3、响应格式

```python
{
    reCode:'000',
    retMsg:'修改成功'
}
```

### 七、删除文章

```python
URL:http://127.0.0.1/article/user
```

#### 1、请求方式

```python
DELETE
```

#### 2、请求格式

```python
{
    '_id':""
}
```

#### 3、响应格式

```python
{
    '':'000';
    'retMsg':'删除成功'
}
```

### 八、搜索文章

```python
URL:http://127.0.0.1/article
```

#### 1、请求方法

```python
GET
```

#### 2.请求参数

| 参数          | 类型   | 含义         | 备注 |
| ------------- | ------ | ------------ | ---- |
| query_keyword | string | 查询的关键字 | 必传 |

#### 3.请求格式

```python
查询字符串
```

```python
例如：
http://127.0.0.1/article?query_keyword=舰队
```

#### 4、响应参数

| 参数        | 类型   | 含义             | 备注 |
| ----------- | ------ | ---------------- | ---- |
| retCode     | string | 响应码           |      |
| retMsg      | string | 响应信息         |      |
| info        | list   | 查询到的信息列表 |      |
| _id         | string | 文章id           |      |
| title       | string | 标题             |      |
| content     | string | 内容             |      |
| author      | string | 作者             |      |
| highlight   | list   | 含高亮介绍       |      |
| update_time | string | 更新时间         |      |

#### 5、响应格式

```python
json
{
    "retCode":"000",
    "retMsg": "查询成功",
    "info":[]
}
例如：
{
    "info": [
        {	
            "_id":"",
            "author": "HUANGJIANFANG",
            "content": "在剩下的三秒钟时间里，章北海转向东方延绪方向，竟笑了一下，说出了几个字：“没关系的，都一样。”三体危机爆发后，章北海与朋友成为第一批中国太空军，人类世界与三体世界巨大的技术鸿沟以及人类科技被三体世界锁死，导致失败主义盛行，但是章北海却对这场未来之战充满了别人无法理解的必胜的信念。在太空军成立初期，章北海检举了朋友 的失败主义心态，并向上级常伟思将军多次建议重视现在军队中的失败主义思潮，重视政治思想工作，甚至提议培养一批拥有必胜信念的优秀政工干部，安排他们冬眠进入未来，以应对那时更严峻的失败主义形势。在冬眠前，章北海精心策划了一起谋杀，被谋杀的是几名在未来宇航技术发展研制方向上有话语权然而思想落后的几位老科学家，老科学家坚持已经发展到尽头的化学动力推进。谋杀行动成功，章北海进去冬眠，而太空战舰研制方向抛弃了化学动力而转向辐射推进型，随后恒星际战舰研制成功。两百多年后，庞大的恒星际战舰的建立使得自大的人类以为未来一站必胜，章北海他们被提前唤醒。而此时两百多年的一项计划败露，一部分军人自愿接受的人类必胜的思想钢印其实是人类必败。由于没人知道现有军人中是否有钢印族，为了防止逃亡，太空舰队决定由冬眠者出任恒星际战舰的执行舰长，权限高于原舰长。章北海被安排到自然选择号上，舰长东方延绪是在太空里长大的一代，是位年轻自信的姑娘。经过学习，章北海知道要想逃离太阳系，需要同时满足两个条件，一个是推进四的指令，既最大速度；另一个是船员进入深海状态，是为了在高速状态下船员不被拍成肉酱。而如果将战舰处于无人遥控状态时，不管里面是否有人是否进入深海状态，战舰都将以最大速度驶向既定目标。在舰长口令移交完毕后，东方惊讶的发现战舰章北海将飞船调为无人遥控状态，为了全舰人员生命安全，她只能同意发布章北海的指令，全舰进入深海状态。自然选择号的逃离震惊了三大舰队（太空舰队分为亚洲舰队欧洲舰队北美舰队），有四艘战舰奉命追击。在逃离了一段距离后，章北海联系了亚洲舰队司令。在两人的对话中我们才得知，章北海那别人无法理解的必胜信念都是伪装的，他是坚定的失败主义者。他只承认自己是逃离而非叛逃，他认为在这场战争中人类必败，他只想为地球保存一艘恒星际飞船为人类保留一个希望。而他这种信念的来源是三体危机之初，他父亲身边聚集的学者的研究，这些学者预言了这两百多年发生的一切，其中就包括人类的必败与灭绝。对话进行的时候，联合舰队正在以胜利姿态迎接水滴的到来。这些新闻也传到了自然选择号上，章北海以飞船不要减速为条件移交了控制权，然后第一次作为一个普通人睡了一觉。等他醒来时，他等来的不是其他舰员的指责，而是包括自然选择号以及四艘追击战舰在内所有舰员的敬礼。原来就在之前，人类太空舰队全军覆没！五艘战舰与太阳系另一端的另外两艘战舰成为仅有的幸存力量，他们有可能成为地球文明唯一的幸存者。他们开始召开公民大会建立星舰地球制定各种章程。然而没过多久，各艘战舰都弥漫着压抑的气氛，资源所限，要想尽快到达可以补给能源的下个星球，只能把所有战舰的资源提供给一艘战舰使用。人类的道德观伦理观、资源的短缺、对其他战舰的猜疑。。种种种种折磨着每一个舰员。终于，东方与另两位副舰长在无言的交流中决心变成魔鬼，攻击另外四艘战舰。而当三人打开武器界面时，发现四个目标已被锁定，是章北海！三人飞速赶往章北海的舱门，只见章北海正在进行操作，他要做这个恶人的角色，一个人下地狱。然而章北海即将发射武器时，自然选择号警报响起，四秒钟后，全舰人员死亡。只慢了几秒钟，另一艘战舰攻击了他们。从传回的影像看，章北海在最后那几秒似乎说了一句“没关系的，都一样”。章北海的故事到此结束，我也终于明白为什么那么多人奉他为男神，他是那个世界当之无愧的男神！对人类的忠诚，极其冷静的理性，缜密的策划，超强的行动力，等等等等。没关系的，都一样。“这是章北海的最后一句话。是的，谁死都一样，只要人类文明的种子保留下来就好，尽管它是以这种黑暗的方式我已经完成了我的使命，尽到了一个军人的责任。 经历了两百年的磨难，心如磐石的章北海在面对死亡的时刻却像一个仁慈的父亲。",
            "highlight": [
                "由于没人知道现有军人中是否有钢印族，为了防止逃亡，太空<b style='color:red' class='ct'>舰队</b>决定由冬眠者出任恒星际战舰的执行舰长，权限高于原舰长。章北海被安排到自然选择号上，舰长东方延绪是在太空里长大的一代，是位年轻自信的姑娘。",
                "自然选择号的逃离震惊了三大<b style='color:red' class='ct'>舰队</b>（太空<b style='color:red' class='ct'>舰队</b>分为亚洲<b style='color:red' class='ct'>舰队</b>欧洲<b style='color:red' class='ct'>舰队</b>北美<b style='color:red' class='ct'>舰队</b>），有四艘战舰奉命追击。在逃离了一段距离后，章北海联系了亚洲<b style='color:red' class='ct'>舰队</b>司令。",
                "对话进行的时候，联合<b style='color:red' class='ct'>舰队</b>正在以胜利姿态迎接水滴的到来。这些新闻也传到了自然选择号上，章北海以飞船不要减速为条件移交了控制权，然后第一次作为一个普通人睡了一觉。",
                "原来就在之前，人类太空<b style='color:red' class='ct'>舰队</b>全军覆没！五艘战舰与太阳系另一端的另外两艘战舰成为仅有的幸存力量，他们有可能成为地球文明唯一的幸存者。他们开始召开公民大会建立星舰地球制定各种章程。"
            ],
            "title": "三体",
            "update_time": "2021-03-31"
        }
    ],
    "retCode": "000",
    "retMsg": "查询成功"
}
```

### 九、展示指定文章列表

```python
http://127.0.0.1:5000/users/6060366bc4435980de3010b8/articles
```

#### 1、请求方法

```python
GET
```

#### 2、请求参数

```python
无
```

#### 3、响应格式

```python
{
    "retCode":"000",
    "retMsg":"查询成功",
    "data":[]
}
```

#### 4、响应格式

```python
{
    "info": [
        {
            "_id": "6073d9bbe1ab864522ce5c7c",
            "content": "对于电影还有作品来说，这是可以永远流传下去的，一部优秀的作品，不管时间如何经历，都会给每一代人很多的看法，尤其是对于喜剧来说，演绎的效果很好，目前优秀的喜剧演员其实并不多，沈腾绝对是其中的一位，人们会很疑惑沈腾是一个自带幽默的人吗？从哪可以看出来？其实绝对就是一个自带幽默的人，从他的日常综艺节目回答就可以看出，我们来具体说一说吧。在很多节目中，其实沈腾的反应速度是真的快，这一点和大张伟差不多，加上自己的话语表情可以给人很幽默的感觉，这是一种高智商，而不是单纯的搞笑而已，很多时候很多场景其实幽默就可以很好地度过，这一点相信大家生活里面也有体会，沈腾其实在晚会就已经有了成绩，那时候叫作开心麻花，不过大家记住的并不是沈腾而是郝建，后面因为夏洛特烦恼而彻底火起来。成功成为一个专业的喜剧演员，就连王晶导演都对他很夸赞，说是另外一种高度的绝对喜剧演员，在很多综艺节目里面的话语反馈很是快，比如一次和宋小宝抢人的时候，就用了经典的话语“小宝，给你比谁都是小白脸”，这句话真的是当时连宋小宝都忍不住笑出来，而且确实就是这样，一个短短的瞬间就可以表达出这样的效果，可见身体这个人的自带幽默很高级的。这就是一种技能，其实每一个人身上都有自己的技能，有时候我们觉得可能并没有什么用处，这是错误的想法，只要开发利用起来在很多方面都可以成就不一样的自己，这就是我们活着的意义，生来就是有价值意义的，不要放弃自己的喜好。",
            "introduce": "对于电影还有作品来说，这是可以永远流传下去的，一部优秀的作品，不管时间如何经历，都会给每一代人很多的看法，尤其是对于喜剧来说，演绎的效果很好，目前优秀的喜剧演员其实并不多，沈腾绝对是其中的一位，人们会...",
            "title": "沈腾私底下也这么搞笑吗？",
            "update_time": "2021-04-10"
        },
        {
            "_id": "6073dad6e1ab864522ce5c7d",
            "content": "当然有办法。先说一句，日方关于放射性氚是废水中唯一的放射性物质的说法是不实的，根据绿色和平组织的调查报告，废水中含有放射性同位素碳-14，其半衰期为5370年，可以进入一切生物体内，可能会损害人类DNA。可怕吧。换位一下，假设，这些核污水是中国的，然后中国政府打算如日本一样的方式将它排入大海，世界会是什么反应？并脑补一下，主导这个世界的欧美国家会怎样对待我们？发动世界范围内海啸一般的批评，抵制，制裁，索赔，甚至借机企图打垮中国……都会是他们情理之中的操作吧。所以，我们完全可以拿来主义，站在道德的高点，联合相关国家，对小日本进行国际批评国际抵制，国际制裁与国际索赔，以实际行动坚决阻止其排放。绝不能打打嘴炮就算了。",
            "introduce": "当然有办法。先说一句，日方关于放射性氚是废水中唯一的放射性物质的说法是不实的，根据绿色和平组织的调查报告，废水中含有放射性同位素碳-14，其半衰期为5370年，可以进入一切生物体内，可能会损害人类DN...",
            "title": "日本政府基本决定将福岛核污水排入大海，真的没办法阻止了吗？",
            "update_time": "2021-04-12"
        },
        {
            "_id": "6073dad9e1ab864522ce5c7e",
            "content": "当然有办法。先说一句，日方关于放射性氚是废水中唯一的放射性物质的说法是不实的，根据绿色和平组织的调查报告，废水中含有放射性同位素碳-14，其半衰期为5370年，可以进入一切生物体内，可能会损害人类DNA。可怕吧。换位一下，假设，这些核污水是中国的，然后中国政府打算如日本一样的方式将它排入大海，世界会是什么反应？并脑补一下，主导这个世界的欧美国家会怎样对待我们？发动世界范围内海啸一般的批评，抵制，制裁，索赔，甚至借机企图打垮中国……都会是他们情理之中的操作吧。所以，我们完全可以拿来主义，站在道德的高点，联合相关国家，对小日本进行国际批评国际抵制，国际制裁与国际索赔，以实际行动坚决阻止其排放。绝不能打打嘴炮就算了。",
            "introduce": "当然有办法。先说一句，日方关于放射性氚是废水中唯一的放射性物质的说法是不实的，根据绿色和平组织的调查报告，废水中含有放射性同位素碳-14，其半衰期为5370年，可以进入一切生物体内，可能会损害人类DN...",
            "title": "日本政府基本决定将福岛核污水排入大海，真的没办法阻止了吗？",
            "update_time": "2021-04-12"
        },
        {
            "_id": "6073dc76e1ab864522ce5c7f",
            "content": "不请自来，好久没用知乎回答问题了。因为手机计算器（大部分情况下的默认计算器），都按照a+b%=a+a*b%或a*(1+b%)计算。至于为什么要这样设计，是因为这会给众多歪果仁带来方便。说实话，我家里的那个计算器的%键好久没用了，要算100元打八折，直接摁100*0.8……但老外们不习惯这样做啦（中国的同志们自带换算），来看看下面几个题：300块钱的餐饮费，10%的小费，一共需要多少钱？2868块钱的iPad，20% off，实际付款多少钱？对于第一个，我们习惯直接300+300*0.1。对于第二个，我们习惯直接2868-2868*0.2。当然，也有更直接的方法，譬如300*1.1。但因为历史原因（初代计算器不支持多次输入，也就是说每次只能输入一次加减乘除），老外们的数学也不咋地，生活中又会出现大量类似上面这样的问题。为了提高效率，老外们就把300+300*10%，简化成了300+10%，直接得出330，类似的，2868-20%=2294.4。你猜怎么着？工作效率大大提升，针不戳！后来就传到了国内，国内的大多数手机计算器都保留了这个传统。当你输入50%+50%的时候，手机先会把前面一个50%转化成0.5（因为它的前面没有数了，于是就默认转成小数，a%=a/100），后一个就理解为「加上前一个数的50%」，于是50%+50%=50%+50%*50%=50%+25%=75%=0.75。",
            "introduce": "不请自来，好久没用知乎回答问题了。因为手机计算器（大部分情况下的默认计算器），都按照a+b%=a+a*b%或a*(1+b%)计算。至于为什么要这样设计，是因为这会给众多歪果仁带来方便。说实话，我家里的...",
            "title": "为什么手机计算器上50%+50%=0.75?",
            "update_time": "2021-04-12"
        },
        {
            "_id": "6073dcc2e1ab864522ce5c80",
            "content": "课堂上老师给我们放过受核辐射感染的人和动物照片，我要是放出来都算污染网络环境，并且那种图片也就是医疗事故等级的和日本核废水比起来就是个弟弟。有人说：他们稀释过了，怕什么?那么问题来了，有人在泳池在游泳池里小便和尿在在水桶里，再把这桶水倒入游泳池有什么区别？​联系一下，《进击的巨人》艾伦最终了消灭岛外80%的人​类。艾伦，这玩意可比地鸣好用多了按照不宣而战的习俗，日本人现在敢说出来，说不定是他们已经倒完了排完57天后的日本人:核废水蔓延不是我们决定的。二十年后日本人：上一代人排的污水关我们什么事？​都鞠躬了你还要怎样，哈哈哈",
            "introduce": "课堂上老师给我们放过受核辐射感染的人和动物照片，我要是放出来都算污染网络环境，并且那种图片也就是医疗事故等级的和日本核废水比起来就是个弟弟。有人说：他们稀释过了，怕什么?那么问题来了，有人在泳池在游泳...",
            "title": "如何看待德国研究机构称，日本核污水 57 天将污染半个太平洋？这将对海洋生态以及周边国家产生什么影响？",
            "update_time": "2021-04-12"
        },
        {
            "_id": "6073dd8be1ab864522ce5c81",
            "content": "这是一个很严肃正经的数学问题。我这里给出严格数学意义上的归纳。你看完之后，会发现其实四维空间没有你想象中的复杂，要理解4维的球形并不是不可能。本文尽量不用公式和术语，方便大家理解。尽管这篇文章不需要任何专业知识也能看懂，但是运气不好的话读上几个小时也是不出人意料的。你看不到不代表它不存在，更不代表我们想象不到；18世纪被提出时就被认为无稽之谈的四维几何在爱因斯坦提出相对论之后，越来越有实际应用价值。在这里并没有引入除公设公理之外任何的假设，整个数学大厦的构建依靠的基础就是如此简单，高维空间也不例外。如果你能够在一张二维纸上具象三维物体，我就能引导你在一本三维“书”上具象四维。空间内的封闭可以是不规则图形，如果用最简单的圆形封闭，本句可作为该问题的答案，但要如何理解呢？四维空间里，就算是最简单的图形，解释起来也要花点功夫。开始前，首先要明确四维空间的定义。说到“四维空间”时，经常会误指相对论中提及的四维时空（三维空间加上时间维度）概念。这种普遍性的误解，是由于相对论的相关科普流行有关。所以在理解这两个概念时，一定要格外小心。详见四维空间为什么不是三维空间加上时间？ Part 1：关于四维球为方便记述，记一点为原点，建立欧氏几何直角坐标系（其实建立球坐标系描述要简单得多，但为更多人所理解，此处用大家熟悉的欧几里得空间建系）。封闭距离设为1。在n维空间就有n个任意两两都垂直的坐标轴。所以在一维空间，球的边缘只有两个点，-1，和1。没错，一维球在我们三维空间来看就是两个点：        .      .虽然可能感觉很奇怪，但从定义上（x²=1的实解）讨论，就是这样， 一维世界的图形除了点线还有什么呢？如果我们将这两个点绕着中心的点在平面旋转一周会得到什么呢？在二维空间，我们可依勾股定理公式得出所有到原点相同距离的点的集合，x²+y²=1²，得到的是无数个实数解，这些点形成二维空间的封闭图形：      〇图形内的点在二维空间内无法不通过此图形而越到外面。如果我们将这个圆绕着中心的线在三维空间旋转一周会得到什么呢？在三维空间，相同道理，x²+y²+z²=1，也得到无数个实数解，这些解的集合是一个三维球，是很易理解，每个点都是上述方程的解",
            "introduce": "这是一个很严肃正经的数学问题。我这里给出严格数学意义上的归纳。你看完之后，会发现其实四维空间没有你想象中的复杂，要理解4维的球形并不是不可能。本文尽量不用公式和术语，方便大家理解。尽管这篇文章不需要任...",
            "title": "二维空间的封闭是圆，三维空间的封闭是球，四维空间的封闭是什么？",
            "update_time": "2021-04-12"
        },
        {
            "_id": "6073df43e1ab864522ce5c82",
            "content": "其实蚂蚁不止在人类身高的高度摔不死，哪怕从巡航高度的飞机上掉下来，也摔不死。民航飞机的巡航高度，一般为8000-12000米。从这个高度掉下去，似乎一切都会碎成渣渣。但是蚂蚁，并不屑于有这样的担忧。原因有二。首先，蚂蚁是真的耐摔。我们都知道，蚂蚁可以搬起比自身重量重400倍的物体。这除了说明蚂蚁力气大，还说明了蚂蚁的身体结构能够承受超强的冲击力。蚂蚁结实的外骨骼和强韧的肌肉让它从空中落下、撞击地面时更不容易受到伤害。其次，蚂蚁从飞机上落下，并不会重重的摔在地面。蚂蚁身轻约0.05g，体型瘦长且不规则，这使他在下落过程中充分受到空气阻力影响。从飞机上掉落后不久，蚂蚁便会保持大约10米每秒的速度匀速下降，经过15分钟左右，才会飘落到地面上。由于蚂蚁非常轻、下落速度并不快，落地时的撞击力约为0.00049N（牛顿）。这个力乘以100倍后（0.049N的力），也才大约相当于举起两个乒乓球的重量。所以，从飞机上落下，撞击到地面，对蚂蚁来说就是挠痒痒而已。其实，有日本科学家从10厘米、1米、10米的高度扔下蚂蚁，也有各国网友从自家屋顶、楼顶扔下蚂蚁。配置了“自动降落系统”的蚂蚁们，都若无其事的平安降落了。但是，万米高空，有零下四五十度的酷寒，气压极低、氧气含量更低，高空风速高达100千米每小时......从飞机上掉落，7分概率落在海里，蚂蚁没能落地，就永远上了天堂。与物理大神隔着一万米距离的小横试着粗略地回答了这个问题，希望能对各位好奇宝宝们有帮助呀。",
            "introduce": "其实蚂蚁不止在人类身高的高度摔不死，哪怕从巡航高度的飞机上掉下来，也摔不死。民航飞机的巡航高度，一般为8000-12000米。从这个高度掉下去，似乎一切都会碎成渣渣。但是蚂蚁，并不屑于有这样的担忧。原...",
            "title": "为什么蚂蚁怎么都摔不死？",
            "update_time": "2021-04-12"
        },
        {
            "_id": "6073e5088336468fb4c150de",
            "content": "眼神到位但不着痕迹。看无间道，几乎每个人都能看出演的痕迹，只有他和杜汶泽看不出来。但不同的是，杜汶泽的不着痕迹会对人物的一些特征表现的不够到位，梁朝伟却不会，如果你仔细看，会发现他每个细节都在呈现这个角色的性格和情绪梁朝伟演的这个角色，有正义感有修养，又受黑道熏陶加上工作压力有些暴力倾向，同时人够狡猾。要把这三个最重要的特点同时呈现是很难的。这种正义感不能太明显，不然卧底就当不成了。暴力倾向要控制，不然与他的正义感和修养相悖，最重要的是人要聪明狡猾，这种聪明狡猾只有在没人的时候才能淋漓尽致的表现在他的眼神和面容上。梁朝伟把这些拿捏的非常好！同时还要表现出做卧底的疲惫感，这种疲惫感也会从他身上深刻的感觉到，但他并没有刻意的用什么表情、动作来表现，只有知道他卧底身份的人，通过仔细的观察推敲，才会发现这些细节",
            "introduce": "眼神到位但不着痕迹。看无间道，几乎每个人都能看出演的痕迹，只有他和杜汶泽看不出来。但不同的是，杜汶泽的不着痕迹会对人物的一些特征表现的不够到位，梁朝伟却不会，如果你仔细看，会发现他每个细节都在呈现这个...",
            "title": "如何评价梁朝伟的演技?",
            "update_time": "2021-04-12"
        }
    ],
    "retCode": "000",
    "retMsg": "查询成功"
}
```

## 喜欢模块数据库设计

1、数据库类型及版本型号

```python
mongodb4.4.4
```

2、字段设计

集合名：like

| 字段             | 含义     | 备注 |
| ---------------- | -------- | ---- |
| _id              | id       | 不传 |
| liked_article_id | 文章id   | 必传 |
| like_user_id     | 用户id   | 必传 |
| like_status      | 喜欢状态 | 必传 |
| create_time      | 创建时间 | 必传 |
|                  |          |      |

3、逻辑描述

点击like按钮，若无喜欢状态 ，则向后端传递 文章id 用户id  喜欢状态 创建时间 管理状态默认为1

再次点击like按钮， 则有喜欢状态，则向后端传递，修改喜欢状态

### 九、添加like

```python
URL: http://127.0.0.1:5000/articles/id/
```

1、请求方式

```python
POST
```

2、请求格式

```python
{
	"author_id":"",
    "user_id":"",
    "like_status":""
}
```

3、响应格式

```python

```

4、响应格式举例

```python

```

十、取消like

```python
URL:http://127.0.0.1:5000/articles/id/like
```

十一、获取like状态

```python
URL:http://127.0.0.1:5000/articles/id/like
```

## 评论数据模块设计

1、数据库类型以及版本号

```python
mongodb4.4.4
```

2、字段设计

```python

```













