---
title: "Hugo 搭博客"
date: 2021-03-15T21:14:10+08:00
lastmod: 2021-04-27T15:21:14+08:00
author: Deabal
toc: true
tags:
  - Go
  - Hugo
---

## 简介

Hugo 是一个开源静态网站生成器。有很多好看的主题，可以快速建站。可以编写模板网页。



## 安装



### Windows

1. 下载 [Hugo](https://github.com/gohugoio/hugo/releases)
2. 找一个路径 `..\Hugo\bin` 放 Hugo，然后配置到系统变量



### Ubuntu

在 Linux 下 `apt-get` 安装的 `Hugo` 包[没有维护](https://github.com/wowchemy/wowchemy-hugo-modules/issues/703) ，是旧版本了，用 `Github` 发布的包来安装。

[包管理的 Hugo](https://packages.ubuntu.com/search?keywords=hugo)

```
xenial (16.04LTS) (web): Fast and flexible Static Site Generator written in Go [universe]
0.15+git20160206.203.ed23711-1: amd64 arm64 armhf i386 powerpc ppc64el s390x
bionic (18.04LTS) (web): Fast and flexible Static Site Generator written in Go [universe]
0.40.1-1: amd64 arm64 armhf i386 ppc64el s390x
focal (20.04LTS) (web): Fast and flexible Static Site Generator written in Go [universe]
0.68.3-1: amd64 arm64 armhf ppc64el s390x
groovy (20.10) (web): Fast and flexible Static Site Generator written in Go [universe]
0.74.3-1: amd64 arm64 armhf ppc64el s390x
hirsute (web): Fast and flexible Static Site Generator written in Go [universe]
0.80.0-6: amd64 arm64 armhf ppc64el s390x
```

1. `wget` [Github最新](https://github.com/gohugoio/hugo/releases)
2. `sudo dpkg -i hugo_0.82.1_Linux-64bit.deb`
3. 如果遇到`Error: Error building site: TOCSS: failed to transform "css/style.css" (text/x-scss). Check your Hugo installation; you need the extended version to build SCSS/SASS.` 还需要下载 extend。



## 使用

1. 创建新的网站

   `hugo new site myhugo`

2. 找一个主题模板

   ```bash
   cd myhugo
   git init
   git submodule add https://github.com/Track3/hermit themes/hermit
   ```

   或者直接 `git clone` 主题也行

   如果用的 submodule ，在另一台新机器上需要：

   1. `git submodule init` 初始化。
   2. 然后 `git submodule update` 来更新获取。
   3. 或者使用递归 clone `git clone --recursive xxx/xx.git`。

3. 把 theme 的名字写入到配置文件

   Linux 下可以这么写，Windows 直接写入文件

   `echo theme = "hermit" >> config.toml`

4. 创建新页面

   `hugo new posts/my-first-post.md`

5. 编写MD

   里面会自带一个 yaml 格式的标签

   ```yaml
   ---
   title: "My First Post"
   date: 2021-03-20T10:49:18+08:00
   draft: true
   toc: false
   images:
   tags: 
     - untagged
   ---
   ```

6. 需要把主题里面的 `exampleSite/config.toml` 复制到根目录，然后按需修改

7. 开启Hugo服务（可以热更新调试）

   `hugo server -D`

8. 导出静态页面

   执行 `hugo` 即可将当前目录的文件导出成静态页面。



## 页前注释

注释可以让这个 MD 获得一定的属性，后台可以根据属性来执行相关操作。

几个默认属性： title, date, draft。

可以自己定义一些 key。



### 种类

有三种语言可以用： YAML, TOML, JSON。默认是YAML，使用 `---` 开头和结尾定义，YAML 使用 `+++` 开头结尾



### 一些用到的预定义标签释义

| 关键词           | 作用                                                         |
| ---------------- | ------------------------------------------------------------ |
| date             | 这篇文章的发表时间                                           |
| lastmod          | 文章的最后修改时间                                           |
| description      | 文章的概要                                                   |
| draft            | 是否草稿，如果 `true` 且不用 `--buildDrafts` 情况下不会发到 `/public` |
| expiryDate       | 过期时间，如果 `true` 且不用 `--buildExpired` 情况下不会发布 |
| images           | 设置关联本页面的图片                                         |
| keywords         | meta 关键字                                                  |
| publishDate      | 如果想以后发布，且不用 `--buildFuture` ，那么不到这个日期不会发布 |
| title            | 文章主标题                                                   |
| weight           | 权重，非零数值，权重高（数字小）的文章会优先出现，如果设置 0 代表未设置 |
| **<taxonomies>** | 分组分类，分为 `tag` 和 `categories` ，为文章打上标签        |

```yaml
---
title: Python DataStructure
date: 2021-03-15T14:24:32+08:00
lastmod: 2021-03-20T14:24:32+08:00
author: Deabal
toc: true
images:
tags:
  - Python
  - DataStructure
---
```





### 用户自定义

可以加上一些自定义的标签，如：`mysignal` ，然后在 HTML 内可以用 `{{.Params.mysignal}}` 来调用。





## 遇到问题

### 路径大小写敏感

在 服务器上，url 路径解析有大小写敏感，因此大写字母开头的文件夹都会404。

在根目录的 `config.yaml` 里面加入 `disablePathTolower = True` 

注意，已经生成了的文件夹需要先删除，否则会自动覆盖原来小写的，文件夹不会改变。



### CORS

`baseURL` 设置成 `https://www.mydomain.com` 的时候，访问 `https://mydomain.com` 会有跨域问题。

```javascript
Access to script at 'https://www.mydomain.com/js/bundle.min.js' from origin 'https://mydomain.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```



### failed to render pages

在 Windows 上运行可以正常运行，但是在 Linux 上执行 hugo 编译出现错误：

```
Error: Error building site: failed to render pages: render of "home" failed: "/var/www/hugo-blog-deabal/layouts/_default/baseof.html:16:97": execute of template failed: template: index.html:16:97: executing "index.html" at <.MediaType.Suffix>: can't evaluate field Suffix in type media.Type
```

发现这是新版本的 Hugo 导致的Linux（hugo v0.82.1-60618210），Windows（hugo v0.81.0-59D15C97+extended）

然后找到 0.82.0 版本里面的 [Note](https://github.com/gohugoio/hugo/releases/tag/v0.82.0) 更新里有改动 `MediaType` 相关的：

>This also means that the old `MediaType.Suffix` and `MediaType.FullSuffix` is moved to `MediaType.FirstSuffix.Suffix` and `MediaType.FirstSuffix.FullSuffix`

所以是主题还没更新到新版本导致的。

只要把 `layouts/_default/baseof.html:16:104` 位置，把 `MediaType.Suffix` 更改为 `MediaType.FirstSuffix.Suffix` 即可。

