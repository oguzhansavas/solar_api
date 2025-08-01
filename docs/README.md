# Chirpy Jekyll Theme

This site uses the [Chirpy Jekyll theme](https://github.com/cotes2020/jekyll-theme-chirpy) - a minimal, responsive and feature-rich Jekyll theme for technical writing.

## Getting Started

### Prerequisites

Follow the instructions in the [Jekyll Docs](https://jekyllrb.com/docs/installation/) to complete the installation of the basic environment. [Git](https://git-scm.com/) also needs to be installed.

### Local Development

To run the site locally:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

### Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Writing Posts

### Creating a New Post

Create a new file in the `_posts` directory with the filename format:

```
YYYY-MM-DD-title.md
```

For example: `2023-08-01-my-first-post.md`

### Post Front Matter

Each post should start with YAML front matter:

```yaml
---
title: Your Post Title
date: 2023-08-01 10:00:00 +0800
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
pin: false
---
```

### Common Front Matter Options

- `title`: The title of your post
- `date`: Publication date and time
- `categories`: Post categories (max 2 levels)
- `tags`: Post tags
- `pin`: Set to `true` to pin the post to the top
- `math`: Set to `true` to enable math expressions
- `mermaid`: Set to `true` to enable mermaid diagrams
- `image`: Post thumbnail image

## Customization

### Site Configuration

Edit `_config.yml` to customize:

- Site title and description
- Author information
- Social media links
- Google Analytics
- Comments system
- Theme settings

### Navigation

The theme automatically generates navigation from your posts' categories and tags. You can also create custom pages by adding markdown files to the root directory.

## Theme Features

- **Responsive Design**: Looks great on desktop, tablet, and mobile
- **Dark/Light Mode**: Automatic theme switching with manual toggle
- **Search**: Built-in search functionality
- **TOC**: Automatic table of contents for posts
- **Categories & Tags**: Organized content browsing
- **Archives**: Chronological post organization
- **SEO**: Search engine optimized
- **Syntax Highlighting**: Code syntax highlighting with copy button
- **Math**: LaTeX math expression support
- **Mermaid**: Diagram and flowchart support

## Resources

- [Chirpy Theme Documentation](https://github.com/cotes2020/jekyll-theme-chirpy)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Demo Site](https://chirpy.cotes.page/)