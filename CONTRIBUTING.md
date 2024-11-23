# CONTRIBUTING GUIDELINES
These guidelines outline the procedures for submitting to the Cyberdream.

First, please read the Code of Conduct

- [Submitting Pull Requests](#submitting-pull-requests)
- [Commit Guidelines](#commit-guidelines)
----
## Submitting Pull Requests
### Getting Started
You should be familiar with the basics of [Git version control](https://www.w3schools.com/git/git_getstarted.asp?remote=github), and have a fork properly set up.

You must always submit Pull Requests with a _dedicated branch_ based on the latest HEAD of the repository.
----
## Commit Guidelines
The Cyberdream conforms to the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

Because this repository is not a typical code repository, the content of commit messages will differ from the norm.

### Format
```
type(scope)!: subject
```
- `type` : the type of the commit is one of the following:
  - `ratify`: new protocols
  - `redact`: removal of protocols
  - `refactor`: changes to protocols
  - `fix`: corrections for spelling, grammar, and names
  - `docs`: improvements to documentation and meta-documents
  - `chore`: other changes that don't match previous types
  - `style`: text style improvements
- `scope` : what sector of the cyberdream the commit impacts. If it impacts many sectons, or none in particular, leave blank without parenthesis.
  - Commit that impacts the I/O Sector:
  ```
  ratify(I/O): modify embassy policy to add region tag restrictions
  ```
  - Commit that impacts many Sectors:
  ```
  refactor: remove duplicate consensus definitions
  ```
- `!`: this goes after the `scope` (or `type` when scope is empty) to indicate that the commit introduces breaking (read: significant) changes.
- `subject`: a brief description of the changes.

### Style
Try to keep the first commit line short. Try keep the commit subject clear and precise enough that what has changed is clear from just reading a changelog. If you need more space, use the commit body.