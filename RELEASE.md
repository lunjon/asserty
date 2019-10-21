# Releasing

Follow the steps below to make a new release.

**1. Set the new version**

Open [\_\_init\_\_.py](./asserty/__init__.py) and set the correct version.

**3. Update the CHANGELOG**

Update the [CHANGELOG](./CHANGELOG.md) accordingly and commit it.

**3. Create the distribution**

```sh
$ make dist
```

**4. Publish the distribution to PyPi.**

```sh
$ make publish
... # enter credentials
```

**4. Tag and push**

```sh
$ git tag -a <version>
$ git push --follow-tags
```