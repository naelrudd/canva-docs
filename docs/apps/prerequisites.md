Source: https://www.canva.dev/docs/apps/prerequisites/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Prerequisites

A list of the skills and tools you need to create an app.

For the most part, developing a Canva App is similar to developing any other web-based software, so any knowledge you have of modern coding standards, tools, and workflows will be beneficial. However, we don't want to assume that everyone has the same background, so this page outlines exactly what you'll need to develop an app.

## TL;DR

You'll need:

* A relatively modern web browser
* A free [Canva](https://www.canva.com/) account
* A command line application, such as **Terminal** on macOS
* An installation of git, and Node.js (`v24`) with npm (`v11`)
* Some knowledge of TypeScript, React, and webpack

## Web browser

You need a relatively modern web browser to develop apps on Canva.

Canva officially supports [the following browsers](https://www.canva.com/en_au/help/technical-requirements/):

* Google Chrome, version 86 or higher
* Mozilla Firefox, version 88 or higher
* Safari, version 13 or higher
* Microsoft Edge, version 89 or higher
* Opera, version 76 or higher

It's worth noting, however, that:

* Some browsers, such as Safari, have security features that interfere with the development workflow.
* Internally, we use the latest version of Google Chrome, so that's the version we can actively support.
* It's easier to preview an app in a standalone browser, rather than using Canva's [desktop app](https://www.canva.com/download).

## Canva account

Canva has a [Developer Portal](https://www.canva.com/developers) for creating, configuring, and otherwise managing apps. Anyone with a standard Canva account has complete access to the Developer Portal. To sign up for Canva, [click here](https://www.canva.com/signup/).

## Terminal

A terminal is an application for running commands that deliver instructions to a computer. This is in contrast to graphical user interfaces (GUIs) that rely on button presses and other forms of interaction. You'll need access to a terminal for various parts of the development workflow, along with some basic command line experience.

All major operating systems have a default terminal:

* On macOS, the default terminal is called **Terminal**.
* On Windows, the default terminal is called **Command Prompt**.
* On Linux, the default terminal depends on the distribution.

## git

git is a version control system that makes it easier to collaborate on and release new versions of code. We use a git repository to distribute a [starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/) for developing apps, so you'll need to know how to clone (download) the repository and, ideally, pull the latest changes as updates to the starter kit are released.

### Installing git

<Tabs storageKey="os">
  <Tab name="macOS">
    To install git on macOS, we recommend using the [Homebrew](https://brew.sh/) package manager:

    1. Install Homebrew:

       ```bash
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
       ```

    2. Run the following command:

       ```bash
       brew install git
       ```

    To learn more about installing git, including alternative options, see [the official documentation](https://git-scm.com/download/mac).
  </Tab>

  <Tab name="Windows">
    To install git on Windows, run the following command:

    ```bash
    winget install --id Git.Git -e --source winget
    ```

    This command assumes that [the winget tool is installed](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
    To learn more about installing git, including alternative options, see [the official documentation](https://git-scm.com/download/windows).
  </Tab>

  <Tab name="Linux">
    To install git on Linux, use the distribution's package manager:

    ```bash
    # Debian/Ubuntu
    apt-get install git

    # Fedora
    dnf install git

    # Arch Linux
    pacman -Syu git
    ```

    To learn more about installing git, including alternative options, see [the official documentation](https://git-scm.com/download/linux).
  </Tab>
</Tabs>

## Node.js (`v24`)

Node.js is a JavaScript runtime that allows JavaScript to run outside of a browser. We use Node.js in the starter kit as it's a key dependency of developer tooling that we rely on, such as [webpack](https://webpack.js.org).

The starter kit requires Node.js `v24`.

### Installing Node.js

To install Node.js, we recommend using [Node Version Manager](https://github.com/nvm-sh/nvm) (nvm). This is a tool for managing multiple versions of Node.js on a single system, which reduces the risk of frustrating versioning errors.

<Tabs storageKey="os">
  <Tab name="macOS">
    1. Install nvm by running the following command:

       ```bash
       curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
       ```

    2. At the root of the starter repo, install Node.js by running the following command:

       ```bash
       nvm install
       ```
  </Tab>

  <Tab name="Windows">
    1. Install nvm by running the following command:

       ```bash
       winget install -e --id CoreyButler.NVMforWindows
       ```

    2. At the root of the starter repo, install Node.js by running the following command:

       ```bash
       nvm install
       ```

    This command assumes that [the winget tool is installed](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
  </Tab>

  <Tab name="Linux">
    1. Install nvm by running the following command:

       ```bash
       curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
       ```

    2. At the root of the starter repo, install Node.js by running the following command:

       ```bash
       nvm install
       ```
  </Tab>
</Tabs>

To verify that the correct version is available in the current terminal session, run the following command:

```bash
node -v
```

If the correct version isn't returned, run the following command from the starter kit directory:

```bash
nvm use
```

This will set the correct version based on the starter kit's [`.nvmrc`](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/blob/main/.nvmrc) file.

**Tip:** You can automatically switch to the appropriate Node.js version by updating your bash or zsh profile to detect the presence of `.nvmrc` files. To learn more, see [the official documentation](https://github.com/nvm-sh/nvm#deeper-shell-integration).

## npm (v11)

npm is a package manager for Node.js. The starter kit uses npm to install and manage dependencies.

npm 11 is bundled with Node.js 24, so no separate installation is required. Once you have Node.js 24 installed, npm is already available.

To verify that npm is available, run the following command:

```shell
npm -v
```

## TypeScript

TypeScript is a superset of JavaScript that adds a variety of features to the language. These features — in particular, static typing — make the language more robust, reducing the likelihood of common errors.

Technically speaking, TypeScript is not required to develop an app. You can use JavaScript. The starter kit is set up to use TypeScript though, and all of the documentation and code samples assume that you're using it.

To learn TypeScript, read [the official documentation](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html).

## React

React is a library for creating fast and interactive user interfaces. It's not strictly required to develop an app, but it's what we use in the starter kit and documentation, and it's required to use the App UI Kit.

To learn React, read [the official documentation](https://react.dev/learn).

## webpack

webpack is what's called a *module bundler*. It's a tool that combines multiple code files into a single file. The process of combining files is known as [bundling](https://www.canva.dev/docs/apps/bundling-apps/) and the file output by a module bundler is known as a *bundle*.

We use webpack in the starter kit, as apps must be uploaded to the Developer Portal as a single file. You shouldn't have to work with webpack directly, but some familiarity may be useful if you want to go off the beaten path.

To learn more about webpack, read [the official documentation](https://webpack.js.org/guides/getting-started/).
