---
title: |
  News
menu:
  main:
    weight: 20
weight: 20
bookCollapseSection: true
---

# What's happened lately in the fluxbox world?

Find announces in here, updates, statements and so on.

{{/*<section>*/}}

{{ range  .Paginator.Pages }}
  {{ .Title }}: {{ .RelPermalink }}
{{ end }}