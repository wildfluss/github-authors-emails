# Collect git author emails 

```bash
time ./author_emails_fast.py jrzaurin/pytorch-widedeep
real	2m48.776s
user	0m3.534s
sys	0m0.712s
```

That will dump pandas dataframe to `jrzaurin-pytorch-widedeep.csv`:

```bash 
$ head jrzaurin-pytorch-widedeep.csv 
sha,author_email,repo
74e9de1d8f24d0f4d126c1f123c1b8a48991fbc5,jrzaurin@gmail.com,jrzaurin/pytorch-widedeep
4325f6017afb9a34ca975c1179ce4f889251facb,jrzaurin@gmail.com,jrzaurin/pytorch-widedeep
```

## How to fetch author emails fast

eg for [jrzaurin/pytorch-widedeep](https://github.com/jrzaurin/pytorch-widedeep):

| How         | time, s       | disk                          | gain               |
|-------------|---------------|-------------------------------|--------------------|
| GitHub API  | 172 = 2m 52.1 |                               |                    |
| `git clone` | 35.9          | 97M --bare or 155M full clone | 20% of GitHub API  |
| the trick   | 2.4           | 632K                          | 1.3% of GitHub API |

`git clone --bare` about the same to `git clone` in time 0m22.245s but 97M vs 155M on disk like this `git clone --bare --filter=blob:none git@github.com:jrzaurin/pytorch-widedeep.git`

The trick is to `git clone --bare --filter=blob:none` because "commit information is stored in commit objects and file names are tracked using tree objects" (and we dont need filenames) https://stackoverflow.com/a/23253517


