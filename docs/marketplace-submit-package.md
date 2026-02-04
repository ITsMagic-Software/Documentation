# Publishing Packages to the ITsMagic Marketplace (GitHub)

This guide explains, step by step, how to publish your package to the **ITsMagic Marketplace**.

All package submissions are made by creating a **Pull Request (PR)** to the official manifest repository:

```
https://github.com/ITsMagic-Software/Packages-Manifest
```

---

## Overview (what you will do)

1. Create a **public GitHub repository** with your package content.  
2. Fork the Marketplace repository.  
3. Create a **manifest file** for your package inside the correct folder.  
4. Add your **media files** (thumbnail + images).  
5. Open a **Pull Request** with your changes.

---

## Step 1: Create a public GitHub repository

Your package files must be stored in a **public GitHub repository**.

- Create a new public repository on GitHub.
- Upload all package files (scenes, scripts, assets, examples).
- Copy the repository URL — this will be used in your manifest.

---

## Step 2: Fork the Marketplace repository

1. Open the manifest repository:
```
https://github.com/ITsMagic-Software/Packages-Manifest
```
2. Click **Fork** to create a copy under your GitHub account.  
3. Clone your fork to your local machine.

---

## Step 3: Create your package manifest

Inside your fork, create the folder structure:

```
packages/yourusername/yourpackage/
```

Then create a file named:

```
packages/yourusername/yourpackage/manifest.json
```

### Example manifest

```json
{
    "titleB64": "U2lzdGVtYSBkZSBzaW11bGHDp8OjbyBkZSBwYW5vIHBhcmEgSXRzIE1hZ2ljIEVuZ2luZS4=",
    "descriptionB64": "U2lzdGVtYSBkZSBzaW11bGHDp8OjbyBkZSBwYW5vIHNpbXBsZXMgcGFyYSBJdHMgTWFnaWMgRW5naW5lLiBwb3NzdWkgc2lzdGVtYSBkZSBjb2xpc29lcyBzaW1wbGVzLHZhcmlhcyBjb25maWd1cmHDp29lcyBlIHVtIHNpc3RlbWEgZGUgZWRpdG9yLHBvc3N1aSBIT1dfVE9fVVNF",
    "tags": "cloth,mesh,physics,malha,pano,fisica",
    "version": 1,
    "repositoryURL": "https://github.com/Vitg1/Mesh-Simulation-System-v1",
    "isTemplate": false,
    "date": "02/02/2026",
    "thumbnail": "capa.png",
    "images": [
        "img2.png",
        "img3.png",
        "img4.png",
        "img5.png",
        "img6.png",
        "img7.png",
        "img8.png"
    ]
}
```

---

## Manifest fields explained

- **`titleB64`**  
  The package title encoded in Base64.

- **`descriptionB64`**  
  The package description encoded in Base64.

- **`tags`**  
  Comma-separated keywords to help users search for your package.

- **`version`**  
  The version of your package. Start at `1` and increase when releasing updates.

- **`repositoryURL`**  
  The URL of your public GitHub repository that contains the package files.

- **`isTemplate`**  
  Set to `true` if this package is a project template; otherwise `false`.

- **`date`**  
  The date of submission in the format `dd/mm/yyyy`.

- **`thumbnail`**  
  The filename of the main image (display thumbnail).

- **`images`**  
  A list of filenames for additional images/screenshots.

---

## Base64: Why and how

The fields `titleB64` and `descriptionB64` must be **Base64-encoded**.  
This ensures safe storage and display of text metadata.

### How to encode text to Base64

You can use any Base64 encoder (online tool, CLI, etc.).

**Example plain text:**
```
Sistema de simulação de pano para Its Magic Engine.
```

Encoded to Base64:
```
U2lzdGVtYSBkZSBzaW11bGHDp8OjbyBkZSBwYW5vIHBhcmEgSXRzIE1hZ2ljIEVuZ2luZS4=
```

Encode your title and description text and place the results in the manifest.

---

## Step 4: Add your media files

Inside your fork of the Marketplace repository, create:

```
media/yourusername/yourpackage/
```

Example:
```
media/Vitg1/Mesh-Simulation-System-v1/
```

Place your images here:

- The `thumbnail` file (as listed in the manifest)
- All files listed under `images[]`

### Image requirements

- Maximum size: **1 MB** per image  
- Accepted formats: **JPG or PNG**  
- Recommended:
  - One thumbnail
  - Up to **8 screenshots**

The folder name must exactly match the path you referenced in your manifest.

---

## Step 5: Commit and open a Pull Request

1. Commit your manifest file under `packages/...`.  
2. Commit your media files under `media/...`.  
3. Push the commits to your fork.  
4. Open a Pull Request:
   - **Base repository:** `ITsMagic-Software/Packages-Manifest`
   - **Base branch:** `main`

In the PR description, include:
- Your package name
- A brief summary of what the package contains

Maintainers will review the Pull Request and merge it upon approval.

---

## Updating your package

When submitting a new version:

- Increase the **`version`** field in your manifest.
- Update any changed images.
- Submit a new Pull Request with the updated files.

---

## Review and approval

All submissions are reviewed by Marketplace moderators.

- Approved PRs will be merged and published.
- If additional changes are needed, moderators will leave feedback on the PR.

---

## Summary

- Each package has a **manifest file** under:
  ```
  packages/<username>/<package>/manifest.json
  ```
- **Title and description** must be **Base64-encoded**.
- Images are stored under:
  ```
  media/<username>/<package>/
  ```
- Packages are published via **GitHub Pull Request**.
