"""Posts 9-12 — runs the generator."""
from generate_posts import run

POSTS = [
{
"slug": "best-posting-times-facebook-pages",
"title": "Best Posting Times for Facebook Pages (Backed by Data)",
"excerpt": "Real data on Facebook page posting times in 2026. Why generic advice fails, how to find your page's actual best times, and how Reels timing differs from photo posts.",
"date": "2026-07-16",
"read_time": "7 min read",
"category": "Strategy",
"cta_title": "Hit your best times automatically",
"cta_body": "Facebook Auto Poster supports per-page schedules so different pages post at their own best times. 7-day free trial.",
"content": """
If you search "best time to post on Facebook" you get a hundred articles that all say roughly the same thing: post at 9am, 1pm, and 3pm on Wednesdays and Thursdays. That advice is broadly correct in the same way "people generally eat dinner around 6pm" is broadly correct. True on average. Useless if you actually want to optimize.

This post covers what real data says about posting times for Facebook pages in 2026, why generic advice fails for specific pages, and how to find the times that actually work for yours.

## Why generic best-time advice fails

The "best times to post" articles you have seen pull data from large aggregations across many pages. They tell you what works for the average page. Your page is not the average page.

The variables that move the "best time" needle for a specific page:

- Audience time zone distribution
- Audience employment status (9-5 office workers, shift workers, retirees, students all have different active windows)
- Content type (Reels, feed videos, photos, links all have different optimal times)
- Posting frequency (a page posting 10 times per day needs different timing strategy than one posting once per day)
- Niche (a sports page peaks on game days, a productivity page peaks weekday mornings)
- Page age and growth stage

A meme page targeting US college students has optimal times that look nothing like a real estate page targeting suburban homeowners. Generic advice averages these together and gives you something that is technically true but functionally wrong.

## What the data actually says (carefully)

A few patterns hold across most Facebook page categories with one caveat: they are starting points, not final answers.

**Reels reach is highest in evenings.** 7pm to 10pm local time tends to outperform daytime for Reels engagement across most pages. The algorithm appears to push Reels harder during high-attention windows when users are scrolling for entertainment.

**Photo posts perform better midday.** 11am to 2pm local time tends to be the photo sweet spot. Lunch break browsing.

**Feed videos perform between Reels and photos.** Mid-morning and early evening both work.

**Weekends shift everything later.** Saturday and Sunday peak engagement is consistently 1-3 hours later than weekday peaks. People sleep in.

**Mondays underperform for most niches.** Tuesday through Friday is the consistent zone for high engagement. Sunday is usually second best for entertainment content.

These are tendencies. They are not rules.

## How to find your page's actual best times

Stop using guides. Use your own data.

**Step 1: Look at Page Insights.** Meta Business Suite shows you "When Your Fans Are Online" by hour and day. This is the most direct signal. Cross-reference this with your historical post performance.

**Step 2: Bucket your posts by hour and look at engagement.** Export your post log if your scheduler supports it. Group posts by hour of day. Calculate average engagement (reactions, comments, shares, video minutes) for each hour. Top three hours equals your real best times.

**Step 3: Test, do not assume.** Run a 4-week experiment with one variable. Same content type, same caption style, same posting frequency. Vary only time of day. After 4 weeks, the time bucket with highest engagement wins.

**Step 4: Re-test every 6 months.** Audience habits shift. Algorithm priorities shift. Your best times in spring may not be your best times in fall.

## Different content needs different times

Once you have your three best time buckets, optimize within those:

**Photos:** Post during your audience's relaxed daytime window. For most US pages, that is 11am to 2pm local time. Photos do not need high-attention windows because they are quick consumption.

**Reels:** Post during your audience's high-attention evening window. For most US pages, that is 7pm to 10pm local time. Reels reach is heavily algorithm-dependent and the algorithm seems to push harder when people are actively scrolling.

**Long videos (over 3 minutes, in-stream ad eligible):** Post when your audience has time to actually watch. Early evening (5pm to 7pm) and weekend mornings (9am to 11am Saturday) tend to outperform.

**Links and external traffic posts:** Mornings work best. People click-out more when they are not winding down.

## Per-page schedules matter

If you run multiple pages, do not use the same schedule across all of them. Different pages have different audiences.

We covered the workflow side of this in a separate post on [scheduling posts to multiple Facebook pages](/blog/posts/schedule-posts-multiple-facebook-pages.html). The point is that a single global schedule is a missed optimization. Tools that support per-page schedules are worth using.

## How frequency interacts with timing

Posting 1x per day: time it perfectly. Pick your single best hour.

Posting 2-3x per day: spread across morning, midday, and evening windows.

Posting 5+ per day: hit every window your audience is active. At this frequency, gaps matter more than peaks.

Posting 10+ per day: maintain steady cadence rather than chasing peaks. Your engagement is averaged across so many posts that timing optimization has diminishing returns.

For most monetized Facebook pages, 2-3 posts per day in the right windows outperforms 6-8 posts spread evenly. Quality of timing beats quantity past a certain point. Our [content monetization eligibility guide](/blog/posts/facebook-content-monetization-eligibility-2026.html) covers the video minutes math for why this works.

## Why automation matters here

The reason most operators do not actually post at their optimal times is not that they do not know. It is that they cannot reliably show up at 11:45am and 8:30pm every day for months on end.

Scheduling automation solves this. Set the times once, point at a content folder, and the posts go out at the right moments whether or not you remember to do it that day.

This is the practical case for using a scheduler. Not that automation magically improves engagement, but that automation actually maintains the schedule you would otherwise let slip.

[Facebook Auto Poster](/) supports per-page schedules with daily post times configured separately for each page. Set page A to 11:45am plus 8:30pm. Set page B to 7am plus 5pm. Schedule once a week. The posting happens automatically across both at their right times.

## Quick reference

For most US-based Facebook pages with mixed content, sensible defaults:

- 11:45am ET (photo or quick video)
- 8:30pm ET (Reel)

For pages with international audiences, schedule against the largest audience timezone using your Insights data.

For Reels-only pages: 7pm to 10pm local time.

For photo-only pages: 11am to 2pm local time.

Use these as starting points. Then look at your own Insights and refine after 4 weeks of consistent posting.
"""
},
{
"slug": "find-facebook-page-id",
"title": "How to Find Your Facebook Page ID (and Why You Need It)",
"excerpt": "Three ways to find your Facebook Page ID in 2026. When you actually need it, common gotchas with Business Manager pages, and what to do with it once you have it.",
"date": "2026-07-23",
"read_time": "5 min read",
"category": "Tutorial",
"cta_title": "Skip the manual setup",
"cta_body": "Facebook Auto Poster connects all your pages via OAuth. No manual Page IDs to copy. 7-day free trial.",
"content": """
Your Facebook Page ID is the unique numerical identifier Facebook assigns to your page. Every page has one. You almost never need to think about it until you do, at which point you need it fast and the answer is non-obvious.

This post covers the three ways to find your Page ID in 2026, why you might need it, and a few common gotchas.

## When you need your Page ID

You need your Page ID when:

- Setting up third-party scheduling tools that ask for a "page ID" rather than just connecting via OAuth
- Using the Facebook Graph API directly
- Filing support tickets where Meta asks for the specific page identifier
- Transferring page ownership between Business Manager accounts
- Setting up some monetization integrations

You do not need your Page ID for:

- Posting through Meta Business Suite (it uses the OAuth connection)
- Using Facebook's own composer
- Most marketing tools that handle authentication via OAuth (they get the ID automatically)

If a tool asks you to paste a Page ID, you need it. Otherwise probably not.

## Method 1: The Page's About section (easiest)

On the web:

1. Go to your Facebook page
2. Click About in the left sidebar (or scroll down on mobile)
3. Scroll to the bottom
4. Find the "Page ID" or "Page transparency" section
5. Copy the number

This works for pages you own and pages you do not own. It is the easiest method.

On mobile in the Facebook app:

1. Open your page in the Facebook app
2. Tap the three-dot menu
3. Tap About
4. Scroll to Page transparency
5. The Page ID is listed

## Method 2: The Page URL (sometimes works)

If your page has a numerical URL like `facebook.com/123456789012345`, that number is your Page ID. Done.

If your page has a custom username like `facebook.com/yourpagename`, the URL itself does not contain the ID. You need to use Method 1 or Method 3.

Most older pages have numerical URLs. Most newer pages and pages with custom usernames do not.

## Method 3: Graph API Explorer (for power users)

If you are setting up a tool that needs your Page ID along with an access token anyway, the Graph API Explorer gives you both at once.

1. Go to developers.facebook.com/tools/explorer
2. Select your app and generate a User Token with `pages_show_list` permission
3. Make a GET request to `/me/accounts`
4. The response is a JSON list of your pages with their IDs and names

This method also gets you the page access tokens you need for tools that operate via the Graph API directly. See our separate guide on [getting Facebook page access tokens manually](/blog/posts/get-facebook-page-access-token-manually.html) for the full walkthrough.

## Common gotchas

**Page ID vs Username vs URL.** These are three different things. Your username is the custom name like "BrandonsBakery". Your URL is the address. Your Page ID is the numerical identifier. Tools that ask for "Page ID" want the number, not the username.

**Multiple IDs for one entity.** A Facebook page and a corresponding Facebook profile linked to it are two different things with two different IDs. If you have a Page that was converted from a Profile, both exist. Use the Page ID, not the Profile ID, for page management tools.

**Business Manager pages.** Pages owned by Business Manager have the same Page ID as personally-owned pages. The ownership structure does not affect the ID. But not all tools see BM-owned pages even with the correct ID. If you copy your ID into a tool and the tool says "page not found", the issue is probably the tool's BM support, not your ID.

**Page transparency hiding.** Some pages have page transparency restricted. If you cannot find the Page ID in the About section, you may need to use Method 3 (Graph API Explorer) instead.

## What to do with your Page ID

Once you have it, common uses:

**Connecting third-party tools:** Paste it into the tool's "Add Page" or "Connect Page" field along with your page access token.

**Filing support tickets:** Include the Page ID in your message so Meta support knows exactly which page you mean.

**Using Graph API directly:** All Graph API calls related to your page use the Page ID as the path segment, like `GET /{page_id}/posts`.

**Backing up data:** If you export page data or download backups, the file names usually reference the Page ID.

For most operators in 2026, the Page ID matters mainly for setting up scheduling tools. After initial setup it lives in the tool's config and you rarely think about it again. See our guide on [scheduling posts to multiple Facebook pages](/blog/posts/schedule-posts-multiple-facebook-pages.html) for the broader workflow.

## Multiple pages, multiple IDs

If you run multiple pages, you have multiple Page IDs. There is no "master ID" that controls all of them. Each page is independent at the ID level.

For multi-page operators, the workflow is usually:

1. Find each page's ID (Method 1)
2. Generate a page access token for each (Method 3 or via your scheduling tool's OAuth)
3. Connect each one to your tools individually

Tools built for multi-page operators ([Facebook Auto Poster](/) included) handle this connection step in bulk via OAuth and never make you paste individual Page IDs. Tools that require manual Page ID entry for each page are usually built around a single-page model and feel clunky when you have more than 2-3 pages. Our guide on [running 5+ Facebook pages without burning out](/blog/posts/run-multiple-facebook-pages-without-burning-out.html) covers the operational side.
"""
},
{
"slug": "get-facebook-page-access-token-manually",
"title": "How to Get a Facebook Page Access Token Manually",
"excerpt": "Step-by-step guide to manually generating a Facebook page access token in 2026. Short-lived vs long-lived tokens, required permissions, and when to use OAuth instead.",
"date": "2026-07-30",
"read_time": "7 min read",
"category": "Tutorial",
"cta_title": "Skip the token dance",
"cta_body": "Facebook Auto Poster uses OAuth so you never have to generate or paste a token manually. 7-day free trial.",
"content": """
Most modern Facebook scheduling tools handle authentication for you. You click "Connect Facebook" and they do the OAuth dance, store the token, and refresh it automatically. You never see the token.

But sometimes you need to manually generate a page access token. Maybe you are using a tool that requires it. Maybe you are testing something via the Graph API directly. Maybe you are debugging a token issue.

This post walks through how to do that in 2026, the gotchas to watch for, and when manual tokens are worse than OAuth.

## When manual tokens matter

You need to generate a page access token manually when:

- A scheduling tool asks you to paste in a "page access token" rather than offering OAuth login
- You are calling the Facebook Graph API directly (for custom scripts, exports, or debugging)
- You are testing whether a Facebook permission actually works for your page
- A tool's OAuth flow is broken and you need a workaround

You do not need manual tokens when:

- A tool offers "Connect Facebook" via OAuth (use OAuth, it is safer)
- Meta Business Suite handles your scheduling
- A standard marketing tool is doing all your posting

If your tool offers OAuth, prefer OAuth. Manual tokens are a last resort.

## Token types: a quick map

Facebook has three relevant token types:

**User access tokens** represent you. They expire quickly (about an hour for short-lived, 60 days for long-lived).

**Page access tokens** represent a specific page. They are derived from a user token. They can be permanent (never expire) if obtained from a long-lived user token.

**App access tokens** represent your Facebook app. They are server-side credentials, not for personal use.

For scheduling tools that ask for a "page access token", you want a long-lived page access token.

## Step-by-step: getting a page access token

This walkthrough uses Facebook's Graph API Explorer. It is the official method.

**Step 1: Open the Explorer.** Go to developers.facebook.com/tools/explorer. Sign in with the Facebook account that admins your page.

**Step 2: Select your Meta app.** In the top right, select your Meta developer app. If you do not have one, you need to create one first at developers.facebook.com/apps.

**Step 3: Generate a User Access Token.** Click "Get Token" then "Get User Access Token". A permissions dialog opens.

**Step 4: Grant the permissions you need.** For page management, you want at minimum:

- `pages_show_list` (lets you see your pages)
- `pages_manage_posts` (lets you create posts)
- `pages_read_engagement` (lets you read page info)

For Reels you also want `pages_manage_posts` plus the Reels-specific permissions that apply to your app's review status.

Check the boxes. Click "Generate Access Token". Approve in the popup.

**Step 5: Switch from User Token to Page Token.** The token you just generated is a user access token. You need to swap it for a page access token.

In the Graph API Explorer, make a GET request to:

```
/me/accounts
```

The response is a JSON list of your pages. Each page entry includes the page name, the page ID, and a page access token.

Copy the `access_token` field for the page you want.

That is your page access token. Short-lived. Expires in about an hour.

**Step 6: Convert to a long-lived token (recommended).** Short-lived tokens are useless for scheduling tools. You need a long-lived token that lasts 60 days.

Make a GET request to:

```
/oauth/access_token?grant_type=fb_exchange_token&client_id={your-app-id}&client_secret={your-app-secret}&fb_exchange_token={short-lived-user-token}
```

Replace the placeholders. The response is a new long-lived user token.

Then redo Step 5 with this new long-lived user token. The page access tokens you get this time are permanent for as long as your app, your permissions, and your account remain in good standing.

You may also want our [Find Your Facebook Page ID guide](/blog/posts/find-facebook-page-id.html) if you are setting up tools that need both pieces.

## Storing tokens safely

A page access token is the equivalent of a password for that page. Anyone with the token can post on the page.

Treat it like a password:

- Do not paste it in chat messages, screenshots, or public forums
- Do not commit it to git
- Store it only in the tool that needs it
- Rotate it (regenerate) if you suspect exposure

If your token gets leaked, regenerate it immediately via the Graph API Explorer. The old token does not get invalidated automatically until you change your password, but the new one will work.

## Common errors and what they mean

**"Invalid OAuth access token"** usually means the token expired. Generate a new one.

**"Permission denied"** means the token does not have the right scope. Re-generate with the correct permissions.

**"Page not found"** with a valid token usually means the page is owned by Business Manager and your token's user is not connected to the BM. Connect the user to the BM and retry.

**"Token rate limited"** means you hit an API call limit. Wait an hour and retry. Real apps need rate-limit handling. For one-off manual tokens this is rare.

## When OAuth wins

Manual tokens are fine for testing, custom scripts, and small operations. They get painful at scale because:

- Long-lived tokens still expire eventually (60 days) and need regeneration
- Regenerating requires going back to the Explorer
- Each new permission scope requires re-generating
- Tokens are easy to leak if you have many of them in different places

Tools that handle OAuth properly do the refreshing automatically. You connect once and forget about it.

For multi-page operations specifically, OAuth is much cleaner. See our guide on [running 5+ Facebook pages without burning out](/blog/posts/run-multiple-facebook-pages-without-burning-out.html) for the operational reasons.

[Facebook Auto Poster](/) uses OAuth for connecting pages. No manual token entry. The page tokens get refreshed automatically as part of the Facebook Login flow.

If you found this post because a tool you are evaluating requires manual token entry, consider whether that requirement signals the tool was built before OAuth was an option. Modern tools rarely make you do this.
"""
},
{
"slug": "bulk-download-images-from-reddit",
"title": "How to Bulk Download Images from Reddit (2026)",
"excerpt": "Methods for bulk downloading images from Reddit in 2026 that still work. Browser extensions, command-line tools, and dedicated scrapers. With ethical and legal context.",
"date": "2026-08-06",
"read_time": "8 min read",
"category": "Tutorial",
"cta_title": "Built-in Reddit scraper",
"cta_body": "Facebook Auto Poster includes a Reddit scraper that pulls images by subreddit and saves post titles as captions. 7-day free trial.",
"content": """
If you run a Facebook page that sources content from Reddit (memes, photos, art, niche communities), manually saving each image from Reddit gets old fast. A subreddit thread with 50 top posts is 50 right-clicks. Multiply by however many subreddits you check.

Bulk downloading from Reddit in 2026 is harder than it was three years ago. Reddit has tightened API access, blocked common scraping endpoints, and shut down many tools that worked previously. This post covers the methods that still work, the legal considerations, and the tradeoffs of each.

## Legal and ethical considerations first

You can technically download any public Reddit image. Whether you can repost it is a different question.

**Reddit's terms** allow personal use of content but restrict commercial use. Reposting someone's image to your monetized Facebook page falls into a gray zone that has gotten more attention from Reddit recently.

**Copyright** belongs to the original creator, not Reddit. If the original poster did not create the image, neither of you have rights to commercially repost it. This is the usual case for memes, where someone screenshots a tweet or finds an old image and posts it.

**Facebook's Content Monetization Policies** explicitly target unoriginal content. Pages that repost without transformation get demonetized fast in 2026. Our [content monetization eligibility guide](/blog/posts/facebook-content-monetization-eligibility-2026.html) covers the rules in detail.

The practical implication: scrape Reddit for inspiration and source material, but transform what you find before posting. Add captions. Combine multiple images. Adapt the message. Direct reposting is increasingly risky.

## Method 1: Manual (still legitimate)

Right-click, save image. For small batches (under 10 images per session) this is fine.

Pros: zero setup, no tools, no risk of bans.

Cons: slow, no metadata preservation, no automation.

Not viable past about 20 images per week.

## Method 2: Browser extensions

Extensions that let you bulk-save images from a Reddit page:

**Imagus** (Firefox, Chrome). Hover-to-preview that also supports bulk download via right-click context menu.

**DownThemAll** (Firefox). Older but still works for downloading all images on a page.

**Image Downloader** (Chrome). Extension that grabs all images from the current tab.

Pros: visual control, easy to use, works without command line.

Cons: still requires you to manually navigate to each subreddit page, slow for many subreddits, captures images but not associated post titles by default.

## Method 3: Command-line tools

For real bulk operations, command-line tools win.

**gallery-dl** (active development, recommended). Install via pip. Run:

```
gallery-dl https://www.reddit.com/r/memes/top
```

Downloads all images from the subreddit's top page. Handles galleries, supports authentication, preserves post metadata in JSON files. Free and open source.

**BDFR (Bulk Downloader for Reddit)** (less actively maintained as of 2026 but still works). Python package with rich configuration. Better for archiving entire subreddits than for quick top-N pulls.

**yt-dlp** is mostly known for YouTube but also handles Reddit posts containing videos. Worth knowing if your content sourcing includes Reddit videos.

Pros: scriptable, fast, supports metadata extraction, free.

Cons: command line required, configuration learning curve, can get rate-limited if you blast many requests.

## Method 4: Dedicated scrapers

Some social media tools include built-in Reddit scrapers as part of their workflow.

[Facebook Auto Poster](/) includes a Reddit scraper that pulls images by subreddit with configurable sort (top, hot, new) and time filter (today, week, month, all time). The scraper downloads images and saves post titles to a captions.txt file in the same folder, so you can use them as caption material when you schedule the content. Output integrates directly with the scheduler so there is no manual file shuffling.

The tradeoff is that dedicated scrapers are part of a larger paid tool. If you only need Reddit scraping and nothing else, command-line tools are cheaper.

For operators using scraped Reddit content as part of a multi-page Facebook posting workflow, the integration with scheduling is the value. See our guide on [running 5+ Facebook pages without burning out](/blog/posts/run-multiple-facebook-pages-without-burning-out.html) for the operational reasoning.

## Preserving post titles as captions

Whichever method you use, capturing the original post title alongside the image is valuable. Post titles often work as Facebook captions with minimal editing.

**gallery-dl** does this by default if you configure it to save metadata. Each downloaded image gets a matching JSON file with the title, author, score, and URL.

**BDFR** also saves JSON sidecar files.

**Facebook Auto Poster's Reddit scraper** writes a single captions.txt file with `filename|caption` lines that the scheduler reads automatically.

**Browser extensions** typically do not preserve metadata. You see the title in the browser but the saved image is just a file.

For monetized pages, having titles preserved cuts caption-writing time substantially. You usually want to revise the title (Reddit titles often have community jokes that do not translate to Facebook), but starting from "an actual title" beats "blank caption box".

## Avoiding rate limits

Reddit applies rate limits to unauthenticated scraping. Symptoms include 429 errors, suddenly empty responses, and IP blocks.

To avoid:

**Add delays between requests.** A 1-2 second delay between calls reduces rate-limit risk substantially. Most CLI tools have a `--sleep` flag.

**Authenticate when possible.** Authenticated requests get higher rate limits. Both gallery-dl and BDFR support OAuth login.

**Do not parallelize aggressively.** Twenty concurrent download workers will trigger Reddit's anti-abuse systems. Two workers is fine.

**Respect robots.txt.** Reddit's robots.txt allows most scraping but explicitly disallows some paths. Stay in the allowed zones.

**Vary your user agent.** Many scrapers default to obvious bot identifiers. Customizing the user agent string to something more browser-like reduces flag risk.

If you get IP-blocked, the block is usually 24 hours. Wait it out. Do not VPN around it as that escalates the response.

## What to do with the downloaded images

Once you have a folder of Reddit images:

1. **Review and curate.** Not every top post is going to fit your page voice. Skip duplicates and off-brand content.

2. **Transform.** Add a caption overlay, crop differently, combine into a carousel, edit slightly. Even small transformations significantly reduce the "unoriginal content" risk on Facebook.

3. **Schedule.** Drop the curated folder into your scheduling tool. Set per-page schedules. See our [best posting times guide](/blog/posts/best-posting-times-facebook-pages.html) for timing strategy.

4. **Track what you posted.** Keep a record of which images came from where so you do not repeat.

The bulk download is the first step. The transformation and scheduling steps are where the actual value of running a page comes from.
"""
},
]

if __name__ == "__main__":
    run(POSTS)
