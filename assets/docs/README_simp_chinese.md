<p align="center">
  <img src="../icon.png" width = "200" height = "200"/>
</p>
<h1 align="center">TuneZ</h1>

<p align="center">
一个基于 Python，每个需要在 Discord 播放音乐的人都可以<strong>开箱即用</strong>的 Discord bot。
</p>

<div align="center">

![Stars](https://img.shields.io/github/stars/NotKeKe/TuneZ-Discord-Bot?style=social)

[![License](https://img.shields.io/badge/license-Apache%20License%202.0-yellow)](LICENSE) <br>
[![Docs](https://img.shields.io/badge/Docs-繁體中文-blue.svg)](../../README.md) 
[![Docs](https://img.shields.io/badge/Docs-English-blue.svg)](README_en.md)

</div>

## 📖 前言
<details>
    <summary>为什么要做这个?</summary>
    <ul>
        <li>
            前阵子有个朋友跟我要了<a href="https://github.com/NotKeKe/Discord-Bot-YinXi">音汐</a>，我后来看了<a href="https://yeecord.com/">YEE式机器龙</a>的<a href="https://yeecord.com/blog/thats-why-i-gave-up-on-music">帖子</a>后才知道，原来现在的音乐机器人已经困难成这样了
        </li>
        <li>
            又因为我其实原本就有音汐了，我就想着 我如果把他关于音乐的代码专门分出来 做音乐机器人，<del>会不会火</del>
        </li>
        <li>
            何况现在 yt-dlp 如果一直从同一个 ip 发送请求的话，也很容易出现 403(没有权限)或者其他错误的请求 <del>(这大概也是为什么音乐机器人越来越少的原因，毕竟稳定的来源确实挺难找的)</del><br>
            但如果每个使用者都只是根据自己的需求 去自建 discord bot，是不是就可以解决这个问题
        </li>
        <li>
            所以说我就做了这个 TuneZ
        </li>
    </ul>
</details>
<details>
    <summary>为什么叫 TuneZ</summary>
    <ul>
        <li>
            其实原因超简单
        </li>
        <li>
            我先随便让 Copilot 帮我想个名字，出现了 Tune。 <br>
            后来想想，大约 2000 年左右的人都会被称作 Z 世代 <br>
            所以又出现了 Z <br>
            结合起来就变成 <strong>TuneZ</strong> 了
        </li>
    </ul>
</details>
<details>
    <summary>会不会有风险?</summary>
    <ul>
        <li>
            答案其实也很简单 自己使用就不会有
        </li>
        <li>
            这种东西通常自己 或者让朋友用一下都不会出啥事
        </li>
        <li>
            除非你选择把它拿去营利 <br>
            那就不能怪我了:) <br>
            我没考虑负责
        </li>
    </ul>
</details>

## 🖥️ Demo
TuneZ 有支援中文，只是因为我的 Discord 预设语言是英文，所以他显示英文
![Demo](demo.png)

## 🌟 特色
<details><summary><strong>自带浅蓝色动画 emojis</strong></summary></details>
<details>
    <summary><strong>可自订 emojis</strong></summary>
    <strong>❗注意图片文件名(不含后缀) 要与 <a href="../emojis/">assets/emojis</a> 里面的文件名一样❗</strong> <small>例如: <code>list.gif</code> → <code>list.png</code></small>
    <ul>
        <li>
            在 Windows 当中，进到 <small><code>C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis</code></small> 可以自己放图片上去
        </li>
        <li>
            在其他环境下，可在 <code>./data/emojis/</code> 中上传自定义图片
        </li>
        <li><strong>
            最后在 Discord 频道里面 使用 <code>/reload_emojis</code> 来重载 emojis
        </strong></li>
    </ul>
</details>
<details>
    <summary><strong>简单易上手</strong></summary>
    <ul>
        <li>
            <strong>Windows 用户</strong>可直接透过 .exe 档开启 TuneZ
        </li>
        <li>
            其他环境的用户，也可以直接使用 <strong>Docker</strong> 启动
        </li>
        <li>
            或是安装好依赖后，直接运行 <code>main.py</code>
        </li>
    </ul>
</details>


## 🛠️ 使用
### 1. 如果你只是单纯希望有一个 Discord 音乐机器人，可以直接邀请[音汐](https://github.com/NotKeKe/Discord-Bot-YinXi)进你的群，这也是我最早开始做的项目。
- [邀请链接](https://discord.com/oauth2/authorize?client_id=990798785489825813)
### 2. 自建 ~~(既然你都点进这个项目了 应该也会选择这个吧)~~ <br>
**❗如果你还没有 Discord Bot，先前往[这个文档](Register_Discord_Bot/Register_Discord_Bot.md)去看教学❗**

**❗除了使用 .exe 以外，其他方法暂时都需要先 克隆/下载该项目❗** <br>
<small>`git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git`</small>

-  Windows
    <details>
        <summary>使用 .exe</summary>
        <ul>
            <li>
                <strong>前往 <a href="https://github.com/NotKeKe/easy-discord-music-bot/releases">Release</a>，下载适合你的版本 (现在应该只有 .exe)</strong>
            </li>
            <li>
                <strong>执行 <code>windows.exe</code> <br></strong>
                执行之后，正常来说会先被关闭，因为它只是要复制必要资源出去。
            </li>
            <li>
                <strong>前往 Roaming 目录</strong> <br>
                通常应该是这样的格式 (把 USERNAME 改成你自己的 应该就可以找到)
                <small><code>C:\Users\USERNAME\AppData\Roaming\Easy Music Bot</code></small>
            </li>
            <li>
                <strong>找到 <code>.env</code>，并使用任何你喜欢的文本编辑器打开</strong>
            </li>
            <li>
                <strong>输入 DISCORD_TOKEN</strong> <br>
                把你刚刚在 Discord Developer 网站里面创建的 Bot 的 Token 贴到 DISCORD_TOKEN，结果应该像这样
                <pre><code class="lang-text"><span class="hljs-attr">DISCORD_TOKEN</span> = MTQ0Nz.....<br><span class="hljs-attr">OWNER_ID</span> = OWNER_ID</code></pre>
                <small>(OWNER_ID 就是你自己的 Discord ID，每个使用者的都不一样，像我的就是 7038778.....，就算不填也没关系，目前只有在需要 reload_emojis 的时候才会用到)</small>
            </li>
            <li>
                <strong>重新开启 <code>windows.exe</code></strong>
            </li>
        </ul>
        现在 你应该可以看到它正常启动了<br>
        <strong>用 /play 来开始播放音乐吧</strong>
        <img src="assets/docs/opened_bot.png">
    </details>

- [Docker](https://www.docker.com/)
    <details>
        <summary>Docker Compose</summary>
        <ul>
            <li>
                将 <code>.env.example</code> 重命名为 <code>.env</code>
                <pre><code class="lang-bash"><span class="hljs-selector-tag">cp</span> <span class="hljs-selector-class">.env</span><span class="hljs-selector-class">.example</span> <span class="hljs-selector-class">.env</span></code></pre>
            </li>
            <li>
                填入你自己的 Discord Bot Token <br>
                大概像这样
                <pre><code class="lang-env"><span class="hljs-attr">DISCORD_TOKEN</span> = MTQ0Nz.....<br><span class="hljs-attr">OWNER_ID</span> = OWNER_ID</code></pre>
                <small>(OWNER_ID 就是你自己的 Discord ID，每个使用者的都不一样，像我的就是 7038778.....，就算不填也没关系，目前只有在需要 reload_emojis 的时候才会用到)</small>
            </li>
            <li>
                创建 logs 和 data 目录 <br>
                (logs 主要用于查看错误，data 用于储存使用者自订播放列表、url 暂存等等......)
                <pre><code class="lang-bash"><span class="hljs-title">mkdir</span> -p <span class="hljs-class"><span class="hljs-keyword">data</span> logs</span></code></pre>
            </li>
            <li>
                使用 docker compose 启动
                <pre><code class="lang-bash">docker compose up <span class="hljs-_">-d</span></code></pre>
            </li>
        </ul>
        <strong>Bot 应该就会成功开起来了!</strong>
    </details>
    
- [uv](https://github.com/astral-sh/uv)
    <details>
        <summary>本项目基于 uv 来管理项目依赖及虚拟环境 (venv)，因此在这里推荐一下 uv</summary>
        <ul>
            <li>
                安装 uv (从以下方法 选一个最适合你的)
                <ul>
                    <li>
                        使用 pip: <pre><code class="lang-bash">pip <span class="hljs-keyword">install</span> uv</code></pre>
                    </li>
                    <li>
                        Windows: <pre><code class="lang-bash"><span class="hljs-symbol">powershell</span> -ExecutionPolicy <span class="hljs-keyword">ByPass </span>-c <span class="hljs-string">"irm https://astral.sh/uv/install.ps1 | iex"</span></code></pre>
                    </li>
                    <li>
                        macOS or Linux: <pre><code class="lang-bash">curl -LsSf http<span class="hljs-variable">s:</span>//astral.<span class="hljs-keyword">sh</span>/uv/install.<span class="hljs-keyword">sh</span> | <span class="hljs-keyword">sh</span></code></pre>
                    </li>
                    <li>
                        更多方法请前往 <a href="https://docs.astral.sh/uv/getting-started/installation/#standalone-installer">uv官网</a>
                    </li>
                </ul>
            </li>
            <li>
                将 <code>.env.example</code> 重命名为 <code>.env</code>
            </li>
            <li>
                在 <code>.env</code> 中，填入你的 Token <br>
                大概像这样
                <pre><code class="lang-env"><span class="hljs-attr">DISCORD_TOKEN</span> = MTQ0Nz.....<br><span class="hljs-attr">OWNER_ID</span> = OWNER_ID</code></pre>
                <small>(OWNER_ID 就是你自己的 Discord ID，每个使用者的都不一样，像我的就是 7038778.....，就算不填也没关系，目前只有在需要 reload_emojis 的时候才会用到)</small>
            </li>
            <li>
                同步虚拟环境
                <pre><code class="lang-bash">uv <span class="hljs-keyword">sync</span></code></pre>
            </li>
            <li>
                执行程序
                <pre><code class="lang-bash">uv <span class="hljs-keyword">run</span><span class="bash"> main.py</span></code></pre>
            </li>
        </ul>
    </details>

## 后言 (?
- **跑成功记得给我一个 Star  我的动力来源阿阿阿啊**
- 不管遇到什么问题 or bug，都可以在 [issue](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues) 提出来
- ~~希望我回答的出来~~