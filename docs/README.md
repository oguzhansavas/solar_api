# Solar Irradiance Forecast API Documentation

This directory contains the Jekyll-based documentation website for the Solar Irradiance Forecast API.

## Structure

- `index.md` - Landing page with API overview
- `getting-started.md` - Quick start guide
- `api-reference.md` - Complete API documentation
- `examples.md` - Real-world examples and use cases
- `coverage.md` - Geographic coverage information
- `support.md` - Support and community resources

## Development

The documentation is built automatically by GitHub Actions and deployed to GitHub Pages.

### Local Development

To run the documentation locally:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

**Note**: The site uses the Just the Docs Jekyll theme which includes features like:
- Sidebar navigation
- Search functionality
- Dark mode support
- Responsive design

If you encounter build issues, ensure you have Ruby 3.0+ and the latest version of Bundler installed.

### Deployment

The site is automatically deployed when changes are pushed to the main branch.

## Theme

The documentation uses the **Just the Docs Jekyll theme** which provides:
- Modern, responsive design with sidebar navigation
- Dark mode support
- Built-in search functionality
- Professional layout optimized for technical documentation
- Custom solar-themed styling integrated with Just the Docs design system

### Theme Features
- Clean, professional appearance
- Mobile-responsive design
- Integrated table of contents
- Syntax highlighting for code examples
- SEO optimized

### Custom Solar Theme Integration
The site maintains its solar energy branding with:
- Solar gradient colors (yellow/orange)
- Custom hero sections and feature cards
- Solar-themed color scheme throughout
- Professional grid layouts for documentation