## GEC (Git Easy Commit)

GEC (Git Easy Commit) is an open source tool that facilitates the creation of standardized commits in Git projects. With GEC, you can create consistent commits following a predefined pattern, making your repository history clearer and more understandable.

### Installation

To install GEC on your system, run the following command in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/hernique33comiitei/gec/main/scripts/install.sh | sh
```

**ATTENTION:** Sometimes it will be necessary to restart the terminal so that the tool can be used.

This command will download and run the GEC installation script directly from the GitHub repository, configuring the tool in your environment.

### How to Use

After successful installation, you can easily use the GEC in your Git repository. Just navigate to the project directory and use the following command to commit:

```bash
git add [archives]
gec
git push
```

The GEC will guide you through the commit creation process, allowing you to select the category, add a message and optionally add a more detailed description. With GEC, you can maintain a consistent pattern for your commit messages, improving collaboration and understanding of project development.

### Contribution

The GEC project is open source and accepts contributions from the community. If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

### License

This project is licensed under the GNU License - see the archive [LICENSE](https://github.com/hernique33comiitei/gec/blob/main/LICENSE) for more details.

### Uninstallation

To uninstall GEC on your system, run the following command in your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/hernique33comiitei/gec/main/scripts/uninstall.sh | sh
```

**ATTENTION:** Sometimes it will be necessary to restart the terminal for the tool to be completely uninstalled.
