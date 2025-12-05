import os
import datetime

# ================= 配置区域 =================
# 1. 这里填入 AI 生成的完整文案 (Phase 2 Script)
SCRIPT_CONTENT = """
Hey there, Yang Hong here. Today is December 3rd, 2025, hoping you stay in good.
There is a very expensive meeting happening in Moscow. Kushner and  Witkoff are sitting across from Putin. They are trying to close a deal to end the war. But while they talk peace in Russia, the bankers in Belgium are panic-stricken about the cost.
We have a massive pot of money sitting in a vault in Brussels. It belongs to Russia. We want to give it to Ukraine. But the Belgians just said "No." And that single word might break the entire financing plan for the war.
So, what is the problem? Why can't we just take the money? To understand this, you have to look at the Financial Plumbing of Europe.
When Russia invaded Ukraine, the West froze about €300 billion of Russian Central Bank assets. Most of that money isn't in New York. It’s in Belgium, sitting at a place called Euroclear. For two years, the plan has been simple: "Use Russia's money to pay for Russia's war." The EU wants to issue a massive loan to Ukraine and use the Russian cash as collateral.
But this week, the Belgian government and the European Central Bank (ECB) hit the brakes. They are refusing to "backstop" the loan. They are terrified that if they touch that money, they break the rules of global finance.
why Belgium is sweating.
Imagine you borrow your friend's car. While you have it, you find a bag with $100,000 of stolen cash in the trunk. Your other friends say: "Hey, let's take that cash and give it to the victim!" It sounds right. But you are the one driving the car. You know that if the mob comes looking for that money, they aren't going to hurt your friends. They are going to burn your car.
Now, let’s cool that down a bit. The "mob" in this scenario isn't hitmen; it's the global financial market. And "burning the car" means a run on the Euro. The ECB is worried that if they seize sovereign assets, countries like China, Saudi Arabia, and Brazil will panic. They might pull their reserves out of Europe because they don't feel safe. The fear isn't about $300 billion today. It's about the trillions that might leave tomorrow.
The data says the EU is trying to raise a €140 billion loan. That is a staggering amount of money. That is enough to run the entire Ukrainian government for two years. But without the legal protection from Belgium, that loan is dead in the water. The plumbing is clogged because nobody wants to be liable for the leak.

If we cannot legally access the Russian money, the bill comes back to the Western taxpayer. And right now? Budgets in Germany and France are tight. The US Congress is fighting over every dollar.
We are prioritizing the "Sanctity of the Euro" over the "Funding of Ukraine." That might be the prudent banking decision. But if that Russian cash stays frozen in the vault, Ukraine might run out of money long before Russia runs out of bombs. The bankers are safe. The frontline is not.


"""

# 2. 这里填入你想用的标题
TITLE_EN = "Why Europe Won't Touch Putin's Money"       # 英文标题（用于文件名和主标题）
TITLE_CN = ""      # 中文副标题
# ===========================================

def create_jekyll_post():
    # 1. 获取当前日期
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%d %H:%M:%S +0800")
    
    # 2. 处理文件名 (将英文标题转为 URL 友好的格式)
    slug = TITLE_EN.lower().replace(" ", "-").replace(":", "").replace("?", "")
    filename = f"_posts/{date_str}-{slug}.md"
    
    # 3. 构建 Jekyll 的头部信息 (Front Matter)
    # 我们把文案中的 "Hook" 等标记稍微美化一下
    formatted_content = SCRIPT_CONTENT.replace("B. The Hook:", "## The Hook 🎣")\
                                      .replace("C. The Structural Context:", "## The Context 🌍")\
                                      .replace("D. The Core Analysis:", "## The Analysis 📊")\
                                      .replace("E. The Verdict:", "## The Verdict ⚖️")

    post_content = f"""---
layout: post
title: "{TITLE_EN}"
subtitle: "{TITLE_CN}"
date: {time_str}
background: '/img/home-bg.jpg'
---

{formatted_content}
"""

    # 4. 保存文件
    # 如果你在本地运行，确保有 _posts 文件夹
    if not os.path.exists("_posts"):
        os.makedirs("_posts")
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(post_content)
    
    print(f"✅ 成功生成文章: {filename}")
    print("👉 下一步：将此文件上传到 GitHub 的 _posts 文件夹，或者直接 git push")

if __name__ == "__main__":
    create_jekyll_post()
