<p align="center">
  <img src="../icon.png" width = "200" height = "200"/>
</p>
<h1 align="center">TuneZ</h1>

<p align="center">
A Python-based Discord bot that works <strong>out-of-the-box</strong> for anyone who needs to play music on Discord.
</p>

<div align="center">

![Stars](https://img.shields.io/github/stars/NotKeKe/TuneZ-Discord-Bot?style=social)

[![License](https://img.shields.io/badge/license-Apache%20License%202.0-yellow)](LICENSE) <br>
[![Docs](https://img.shields.io/badge/Docs-繁體中文-blue.svg)](../../README.md) 
[![Docs](https://img.shields.io/badge/Docs-简体中文-blue.svg)](README_simp_chinese.md)

</div>

## 📖 Preface
<details>
    <summary>Why did I make this?</summary>
    <ul>
        <li>
            A while back, a friend asked me for <a href="https://github.com/NotKeKe/Discord-Bot-YinXi">YinXi</a> (my other bot). Later, I read a <a href="https://yeecord.com/blog/thats-why-i-gave-up-on-music">post</a> by <a href="https://yeecord.com/">YeeCord</a> and realized just how difficult maintaining music bots has become these days.
        </li>
        <li>
            Since I already had YinXi, I thought: if I just split out the music-related code and made a dedicated music bot, <del>would it go viral?</del>
        </li>
        <li>
            Plus, if yt-dlp keeps sending requests from the same IP, it's super easy to get hit with 403 (Forbidden) errors or other issues. <del>(This is probably why there are fewer and fewer music bots; finding a stable source is genuinely tough)</del><br>
            But if every user just self-hosts their own Discord bot based on their own needs, wouldn't that solve the problem?
        </li>
        <li>
            So, I made TuneZ.
        </li>
    </ul>
</details>
<details>
    <summary>Why is it called TuneZ?</summary>
    <ul>
        <li>
            The reason is actually super simple.
        </li>
        <li>
            I just asked Copilot to come up with a name, and it gave me "Tune". <br>
            Then I thought, people born around the year 2000 are called Gen Z. <br>
            So "Z" appeared. <br>
            Combine them, and you get <strong>TuneZ</strong>.
        </li>
    </ul>
</details>
<details>
    <summary>Are there any risks?</summary>
    <ul>
        <li>
            The answer is also simple: not if you use it for yourself.
        </li>
        <li>
            Usually, nothing bad happens with this kind of stuff if you use it yourself or just let friends use it.
        </li>
        <li>
            Unless you decide to use it for profit. <br>
            Then you can't blame me :) <br>
            I'm not taking responsibility for that.
        </li>
    </ul>
</details>

## 🖥️ Demo
TuneZ supports Chinese. It's just showing English because my Discord default language is English.
![Demo](demo.png)

## 🌟 Features
<details><summary><strong>Comes with light blue animated emojis</strong></summary></details>
<details>
    <summary><strong>Customizable emojis</strong></summary>
    <strong>❗Pay attention to image filenames (excluding extension); they must match the filenames in <a href="../emojis/">assets/emojis</a>❗</strong> <small>Example: <code>list.gif</code> → <code>list.png</code></small>
    <ul>
        <li>
            On Windows, go to <small><code>C:\Users\USERNAME\AppData\Roaming\Easy Music Bot\data\emojis</code></small> and you can put your own images there.
        </li>
        <li>
            In other environments, upload custom images to <code>./data/emojis/</code>.
        </li>
        <li><strong>
            Finally, use <code>/reload_emojis</code> in your Discord channel to reload the emojis.
        </strong></li>
    </ul>
</details>
<details>
    <summary><strong>Simple and easy to start</strong></summary>
    <ul>
        <li>
            <strong>Windows users</strong> can open TuneZ directly via the .exe file.
        </li>
        <li>
            Users in other environments can launch it directly using <strong>Docker</strong>.
        </li>
        <li>
            Or, after installing dependencies, just run <code>main.py</code>.
        </li>
    </ul>
</details>


## 🛠️ Usage
### 1. If you simply want a Discord music bot, you can just invite [YinXi](https://github.com/NotKeKe/Discord-Bot-YinXi) to your server. This was my very first project.
- [Invite Link](https://discord.com/oauth2/authorize?client_id=990798785489825813)
### 2. Self-hosting ~~(Since you clicked on this project, I assume this is what you'll choose)~~ <br>
**❗If you don't have a Discord Bot yet, go to [this file](Register_Discord_Bot/Register_Discord_Bot.md) for a tutorial first❗**

**❗Except for using the .exe, other methods currently require you to Clone/Download the project first❗** <br>
<small>`git clone https://github.com/NotKeKe/TuneZ-Discord-Bot.git`</small>

-  Windows
    <details>
        <summary>Using .exe</summary>
        <ul>
            <li>
                <strong>Go to <a href="https://github.com/NotKeKe/easy-discord-music-bot/releases">Releases</a> and download the version that suits you (currently there should only be an .exe)</strong>
            </li>
            <li>
                <strong>Run <code>windows.exe</code> <br></strong>
                After running it, it will normally close itself first because it's just copying necessary resources out.
            </li>
            <li>
                <strong>Go to the Roaming directory</strong> <br>
                It should usually be in this format (change USERNAME to your own and you should find it):
                <small><code>C:\Users\USERNAME\AppData\Roaming\Easy Music Bot</code></small>
            </li>
            <li>
                <strong>Find <code>.env</code> and open it with any text editor you like.</strong>
            </li>
            <li>
                <strong>Enter your DISCORD_TOKEN</strong> <br>
                Paste the Bot Token you just created on the Discord Developer site into DISCORD_TOKEN. The result should look like this:
                <pre><code class="lang-text"><span class="hljs-attr">DISCORD_TOKEN</span> = MTQ0Nz.....<br><span class="hljs-attr">OWNER_ID</span> = OWNER_ID</code></pre>
                <small>(OWNER_ID is your own Discord ID. Everyone's is different. Mine is 7038778.... It's fine even if you leave it blank; currently, it's only used when `reload_emojis` is needed.)</small>
            </li>
            <li>
                <strong>Re-open <code>windows.exe</code></strong>
            </li>
        </ul>
        Now, you should see it starting up normally.<br>
        <strong>Use /play to start playing music!</strong>
        <img src="assets/docs/opened_bot.png">
    </details>

- [Docker](https://www.docker.com/)
    <details>
        <summary>Docker Compose</summary>
        <ul>
            <li>
                Rename <code>.env.example</code> to <code>.env</code>
                <pre><code class="lang-bash"><span class="hljs-selector-tag">cp</span> <span class="hljs-selector-class">.env</span><span class="hljs-selector-class">.example</span> <span class="hljs-selector-class">.env</span></code></pre>
            </li>
            <li>
                Fill in your own Discord Bot Token <br>
                Something like this:
                <pre><code class="lang-env"><span class="hljs-attr">DISCORD_TOKEN</span> = MTQ0Nz.....<br><span class="hljs-attr">OWNER_ID</span> = OWNER_ID</code></pre>
                <small>(OWNER_ID is your own Discord ID. Everyone's is different. Mine is 7038778.... It's fine even if you leave it blank; currently, it's only used when `reload_emojis` is needed.)</small>
            </li>
            <li>
                Create logs and data directories <br>
                (logs are mainly for checking errors; data is for storing user custom playlists, url cache, etc...)
                <pre><code class="lang-bash"><span class="hljs-title">mkdir</span> -p <span class="hljs-class"><span class="hljs-keyword">data</span> logs</span></code></pre>
            </li>
            <li>
                Start with docker compose
                <pre><code class="lang-bash">docker compose up <span class="hljs-_">-d</span></code></pre>
            </li>
        </ul>
        <strong>The Bot should be up and running successfully!</strong>
    </details>
    
- [uv](https://github.com/astral-sh/uv)
    <details>
        <summary>This project uses uv to manage dependencies and virtual environments (venv), so I'm recommending uv here.</summary>
        <ul>
            <li>
                Install uv (Pick the method that suits you best)
                <ul>
                    <li>
                        Using pip: <pre><code class="lang-bash">pip <span class="hljs-keyword">install</span> uv</code></pre>
                    </li>
                    <li>
                        Windows: <pre><code class="lang-bash"><span class="hljs-symbol">powershell</span> -ExecutionPolicy <span class="hljs-keyword">ByPass </span>-c <span class="hljs-string">"irm https://astral.sh/uv/install.ps1 | iex"</span></code></pre>
                    </li>
                    <li>
                        macOS or Linux: <pre><code class="lang-bash">curl -LsSf http<span class="hljs-variable">s:</span>//astral.<span class="hljs-keyword">sh</span>/uv/install.<span class="hljs-keyword">sh</span> | <span class="hljs-keyword">sh</span></code></pre>
                    </li>
                    <li>
                        For more methods, visit the <a href="https://docs.astral.sh/uv/getting-started/installation/#standalone-installer">uv official site</a>
                    </li>
                </ul>
            </li>
            <li>
                Rename <code>.env.example</code> to <code>.env</code>
            </li>
            <li>
                In <code>.env</code>, fill in your Token <br>
                Something like this:
                <pre><code class="lang-env"><span class="hljs-attr">DISCORD_TOKEN</span> = MTQ0Nz.....<br><span class="hljs-attr">OWNER_ID</span> = OWNER_ID</code></pre>
                <small>(OWNER_ID is your own Discord ID. Everyone's is different. Mine is 7038778.... It's fine even if you leave it blank; currently, it's only used when `reload_emojis` is needed.)</small>
            </li>
            <li>
                Sync the virtual environment
                <pre><code class="lang-bash">uv <span class="hljs-keyword">sync</span></code></pre>
            </li>
            <li>
                Run the program
                <pre><code class="lang-bash">uv <span class="hljs-keyword">run</span><span class="bash"> main.py</span></code></pre>
            </li>
        </ul>
    </details>

## Postscript (?
- **Remember to give me a Star if you succeed! It's my source of motivation!**
- No matter what problems or bugs you encounter, you can raise them in [issue](https://github.com/NotKeKe/TuneZ-Discord-Bot/issues)
    - ~~Hope I can answer them~~