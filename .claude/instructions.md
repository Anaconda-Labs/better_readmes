# Anaconda Organization - Development Standards

**You are working in an Anaconda environment.** This organization uses conda-first development practices. Follow these guidelines unless explicitly instructed otherwise.

---

## Understanding Conda: Beyond a Package Manager

**Conda is a user-space distribution system, not just a package manager.**

Conda manages **entire runtime environments** — including:
- Pre-compiled C/C++/Fortran libraries
- GPU runtimes (CUDA, cuDNN)
- Compilers and toolchains
- Cross-language dependencies (Python, R, Julia, etc.)
- System utilities and DevOps tools

### The Key Distinction

- **PyPI/pip**: Distributes Python-only source distributions and wheels. Assumes your system already has compilers, headers, and native dependencies.
- **Conda**: Delivers complete binary builds with full dependency resolution across programming languages and platforms.

**Analogy:** pip is like a car stereo in that it needs a system to plug into. Conda is like the whole car in that it is a complete, self-contained system with runtime, fuel system, and all.

### Why This Matters for Anaconda

Anaconda's ecosystem depends on **binary reproducibility** and **cross-language stability**. Conda ensures:
- ✅ Fast, compiler-free installs
- ✅ ABI (Application Binary Interface) and dependency consistency
- ✅ Portable, self-contained environments
- ✅ Auditable provenance (build recipes, source hashes, and checksums)
- ✅ Forward compatibility across OS versions

---

## Conda Package Management (PRIMARY)

### Default Behavior: Conda First

**Always use conda for package management as the first choice:**

NOTE: You may need to provide the full path to the conda executable if it's not in your PATH.
Additionally, you may need to use something like `/opt/miniconda3/envs/anaconda-claude-code/bin/python`

```bash
# ✅ CORRECT - Use conda with 'defaults' channel (Anaconda's curated packages)
conda install <package-name>

# ✅ ALSO CORRECT - Explicit defaults channel
conda install -c defaults <package-name>

# ✅ ACCEPTABLE - conda-forge if not in defaults
conda install -c conda-forge <package-name>

# ⚠️ LAST RESORT - Only if package unavailable in conda
# But even then, do the pip install from within a conda environment
pip install <package-name>
```

### Channel Priority and Hygiene

**Internal Anaconda Policy:**

1. **defaults** channel first - Anaconda's curated, tested packages
2. **conda-forge** channel - Community packages (if not in defaults)
3. **pip** - Only when package doesn't exist in conda channels

**Channel Hygiene Best Practices:**
- Explicitly list your channels in `environment.yml`
- Stick to one "ecosystem" per environment (defaults *or* conda-forge, not both mixed extensively)
- Avoid mixing large numbers of packages from multiple channels
- Always install **conda packages first**, then **pip** packages
- Document every pip-only dependency under the `pip:` section in `environment.yml`

**Security Note:** Avoid arbitrary third-party channels without security review.

### Why Conda First?

- **Binary packages**: Pre-compiled, faster installation (no compilation)
- **Dependency resolution**: SAT-based solver handles complex cross-language dependencies
- **Multi-language support**: Manages Python + C/C++/Fortran/R dependencies together
- **Testing**: Anaconda's defaults channel is curated and tested for compatibility
- **Performance**: Optimized builds with Intel MKL or OpenBLAS for numerical packages
- **Portability**: Built against oldest supported system libraries for forward compatibility

---

## Virtual Packages and Compatibility Constraints

Conda auto-detects system properties (like glibc, CUDA, CPU architecture) and exposes them as **virtual packages**, which act as environment constraints during solving.

```bash
# View your system's virtual packages
conda info

# Common virtual packages:
# __glibc        - Linux C library version (e.g., 2.17)
# __osx          - macOS version
# __win          - Windows version
# __cuda         - CUDA GPU driver version
# __archspec     - CPU architecture (x86_64, aarch64)
# __linux        - Linux platform indicator
# __unix         - Unix-like platform indicator
```

**Why This Matters:**
When you install pytorch, tensorflow, or any GPU package, conda ensures the selected build matches your driver and hardware — preventing runtime mismatches and ABI incompatibilities.

These virtual packages are NOT installed files—they're ephemeral host facts injected into the solver to ensure compatibility.

---

## Environment Management

### Creating Environments

**Always use conda environments, never venv:**

```bash
# ✅ CORRECT - Create conda environment
conda create -n myproject python=3.11
conda activate myproject

# ✅ ALSO CORRECT - Miniconda is fully supported
# (Miniconda is Anaconda's minimal installer - we use it internally)

# ❌ AVOID - Do not use venv/virtualenv by default
# python -m venv myenv  ← Only if explicitly requested
```

### Environment Files

**Prefer `environment.yml` over `requirements.txt`:**

```bash
# ✅ Export conda environment (concise - recommended)
conda env export --from-history > environment.yml

# ✅ Export conda environment (full - includes all dependencies)
conda env export > environment-full.yml

# ✅ Create from environment file
conda env create -f environment.yml

# ✅ Update existing environment
conda env update -f environment.yml --prune
```

**Example `environment.yml` structure:**
```yaml
name: myproject
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.11
  - numpy=1.26.*
  - pandas>=2.0
  - scikit-learn
  - pip
  - pip:
      - some-pip-only-package
      - another-pypi-package
```

**Best Practices:**
- Pin major versions for stability (e.g., `python=3.11`, `numpy=1.26.*`)
- Use `--from-history` to capture only explicitly installed packages
- Document pip dependencies in the `pip:` section
- Commit `environment.yml` to version control

---

## Reproducibility and Lockfiles

### Why Locking Matters

`environment.yml` specifies what you *want* (with version ranges).  
A **lockfile** captures exactly *what you got* — precise versions, hashes, platforms, and provenance.

**Benefits of Lockfiles:**
- **Reproducibility**: Rebuild identical environments across time, teams, and machines
- **Supply chain security**: Locked hashes verify package integrity and bind all embedded metadata immutably
- **Reliability**: No surprises from solver changes or package updates
- **Audit trail**: Know exactly what was installed and when

### Creating Lockfiles

```bash
# Install conda-lock
conda install -c conda-forge conda-lock

# Generate lockfiles for multiple platforms
conda-lock -f environment.yml -p linux-64 -p osx-64 -p win-64

# Install from lockfile (deterministic)
conda-lock install --name myproject conda-lock.yml

# Update specific packages
conda-lock --update numpy pandas
```

**For Modern Workflows (pixi):**
```bash
# pixi automatically manages lockfiles
pixi init
pixi add numpy pandas scikit-learn
# pixi.lock is automatically created and updated
```

### Internal Guidance

- **Commit lockfiles** to your repo for audit and reproducibility
- Treat lockfiles like `requirements.txt` in pip projects — version-controlled, reviewed, and tested before merge
- Update intentionally and test thoroughly after updating dependencies
- For production environments, always use lockfiles

---

## The Three-Layer Packaging Model

Conda sits between OS-level tooling and language registries. Understanding this model helps you make better decisions about which tool to use.

```
┌────────────────────────────────────────┐
│  Layer 3: Language Registries          │
│  pip, npm (pure-language libraries)    │
│  ✅ Fast iteration                      │
│  ✅ Huge ecosystem                      │
│  ✅ Latest releases                     │
├────────────────────────────────────────┤
│  Layer 2: Conda Distribution           │
│  Multi-language runtimes + binaries    │
│  ✅ Binary dependencies                 │
│  ✅ Cross-language coherence            │
│  ✅ Optimized builds                    │
│  ✅ GPU/CUDA support                    │
├────────────────────────────────────────┤
│  Layer 1: Operating System             │
│  Kernel, glibc, core system utilities  │
│  ✅ Platform baseline                   │
│  ✅ Hardware drivers                    │
└────────────────────────────────────────┘
```

### Best Practice Workflow

1. **Base layer**: OS / container baseline (Layer 1)
2. **Add core dependencies** via conda: compiled libraries, runtimes, cross-language packages (Layer 2)
3. **Add pure-Python packages** with pip inside the conda environment (Layer 3)

**Example:**
```bash
# Create conda environment with core dependencies (Layer 2)
conda create -n myapp python=3.11 numpy scipy pandas jupyter
conda activate myapp

# Then add pure-Python packages with pip (Layer 3)
pip install requests flask fastapi pydantic
```

**Why This Works:**
- Optimized scientific libraries from conda
- Latest pure-Python packages from PyPI
- No dependency conflicts
- Best of both worlds

> This layered view helps avoid dependency overlap and keeps environments portable across platforms.

---

## CRITICAL: Python Binary Paths

### Always Use Full Paths to Python Binaries

When executing Python scripts, linting, testing, or any Python operations, **always use the full path to the Python binary in the active conda environment.**

**❌ INCORRECT - Relative or system Python:**
```bash
python script.py
python -m pytest
/usr/bin/python script.py
```

**✅ CORRECT - Full conda environment path:**
```bash
/opt/miniconda3/envs/myproject/bin/python script.py
/opt/miniconda3/envs/myproject/bin/python -m pytest
/home/user/miniconda3/envs/myproject/bin/python script.py
```

### How to Get the Correct Python Path

```bash
# Get active environment's Python
which python
# Output: /opt/miniconda3/envs/myproject/bin/python

# Use that full path in commands
$(which python) script.py

# Or store it first
PYTHON_BIN=$(which python)
$PYTHON_BIN -m pytest tests/
```

### Why Full Paths Matter

- **Ensures correct environment**: No ambiguity about which Python is running
- **Avoids PATH issues**: Works even if PATH is misconfigured
- **Explicit is better**: Clear what environment is being used
- **Conda best practice**: Guarantees environment isolation

### Common Full-Path Commands

```bash
# Running scripts
/opt/miniconda3/envs/myproject/bin/python app.py

# Running modules
/opt/miniconda3/envs/myproject/bin/python -m pytest
/opt/miniconda3/envs/myproject/bin/python -m pip list

# Running installed console scripts
/opt/miniconda3/envs/myproject/bin/pytest
/opt/miniconda3/envs/myproject/bin/black .
/opt/miniconda3/envs/myproject/bin/mypy src/
```

---

## Environment Activation Best Practices

```bash
# ✅ Activate before working
conda activate myproject

# ✅ Check active environment
conda info --envs
# The active environment has a * next to it

# ✅ Verify Python path after activation
which python
# Should show: /path/to/conda/envs/myproject/bin/python

# ✅ List packages in active environment
conda list

# ✅ See environment info and virtual packages
conda info
```

---

## Performance Packages: Conda's Optimized Builds

Many scientific and ML packages contain compiled C/Fortran code and rely on optimized math libraries (BLAS/LAPACK).

### Why Conda for Performance-Critical Packages

**Conda advantages:**
- Pre-built with Intel MKL or OpenBLAS (optimized BLAS implementations)
- ABI-compatible across Python versions
- Built with platform-specific optimizations (AVX2, AVX-512)
- No compilation required at install time

**Installing these with pip often means:**
- Slower generic builds or compilation from source
- Missing optimizations
- Potential compilation errors if system dependencies are missing

### Always Use Conda For These Packages

**Scientific Computing:**
- numpy, scipy, pandas, scikit-learn
- numba, cython, bottleneck

**Visualization:**
- matplotlib, seaborn, plotly, bokeh
- pillow, opencv

**Machine Learning:**
- pytorch, tensorflow, jax
- xgboost, lightgbm, catboost

**Data I/O:**
- netcdf4, h5py, zarr, pyarrow
- sqlalchemy, psycopg2

```bash
# ✅ MUCH FASTER - Optimized binaries (MKL, BLAS)
conda install numpy scipy scikit-learn pandas

# ❌ SLOWER - Generic builds or compiles from source
pip install numpy scipy scikit-learn pandas
```

**Why Internal Developers Care:**
Optimized binaries ensure performance parity across macOS, Linux, and Windows builds in Anaconda distributions. This is critical for our users' experience.

**Real-world impact:** conda can install numpy+scipy in seconds vs. minutes with pip (and with better performance).

---

## Beyond Python: Conda for Tooling and DevOps

Conda isn't just for Python and data science. Many infrastructure and DevOps tools are available as conda packages.

```bash
# Kubernetes / Cloud Native
conda install -c conda-forge kubectl helm k3d terraform

# Infrastructure as Code
conda install -c conda-forge terraform packer ansible

# Modern CLI tools
conda install -c conda-forge ripgrep fd-find bat jq yq just

# Git tools
conda install -c conda-forge git git-lfs gh lazygit gitui

# Container tools
conda install -c conda-forge docker-compose podman

# Text processing
conda install -c conda-forge httpie curl wget
```

### Why Use Conda for DevOps Tools?

- **Version-controlled**: Lock tool versions alongside application dependencies
- **Cross-platform**: Works consistently on Linux, macOS, Windows
- **No system conflicts**: Isolated from system package managers
- **Reproducible**: Team uses exact same tool versions
- **No root required**: Install without administrator privileges

---

## When to Use Pip (Inside Conda)

**Pip is acceptable in these scenarios:**

1. **Package only available on PyPI**
   ```bash
   conda activate myproject
   pip install some-pypi-only-package
   ```

2. **Pure-Python packages** with no compiled dependencies
   ```bash
   pip install requests flask fastapi pydantic
   ```

3. **Installing in development mode**
   ```bash
   pip install -e .
   ```

4. **User explicitly requests pip**

**Important:** Always use pip **inside** an active conda environment, never globally.

### Mixing Conda and Pip Safely

If you must combine them:

1. **Install ALL conda packages first**
2. **Then run `pip install`** for PyPI-only packages
3. **Document pip installs** under the `pip:` section in `environment.yml`
4. **Avoid re-running `conda install`** after pip — it can overwrite pip-installed dependencies

**Example:**
```bash
# Step 1: Install conda packages
conda install numpy scipy pandas jupyter

# Step 2: Install pip packages
pip install some-pypi-only-package

# Step 3: Document in environment.yml
```

```yaml
dependencies:
  - numpy
  - scipy
  - pandas
  - jupyter
  - pip
  - pip:
      - some-pypi-only-package
```

---

## Package Installation Decision Tree

```
Need to install a package?
│
├─ Is it a performance/scientific package (numpy, pytorch, etc.)?
│  └─ YES → ALWAYS use conda (conda install <package>)
│
├─ Does it have compiled code or native dependencies?
│  ├─ YES → Use conda first
│  │   ├─ In defaults? → conda install <package>
│  │   ├─ In conda-forge? → conda install -c conda-forge <package>
│  │   └─ Not available? → pip install (inside conda env)
│  │
│  └─ NO (pure Python) → Check availability
│      ├─ In conda? → conda install <package>
│      └─ Only on PyPI? → pip install (inside conda env)
│
└─ Creating an environment?
   └─ ALWAYS use conda/mamba/pixi
      ❌ Never use venv in Anaconda workflows
```

---

## Modern Solver and CI/CD Optimizations

### Use the libmamba Solver # NOTE: YOU DO NOT NEED TO INSTALL THIS AS LONG AS USER HAS AN UPDATED CONDA. ALWAYS CHECK THE CONDA VERSION FIRST TO SEE IF LIBMAMBA SOLVER IS ALREADY INSTALLED BY DEFAULT

The **libmamba solver** is significantly faster and more reliable than the classic solver:

```bash
# Install libmamba solver
conda install -n base conda-libmamba-solver

# Set as default solver
conda config --set solver libmamba

# Or use for single command
conda install --solver=libmamba <package>
```

**Why libmamba?**
- 10-100x faster dependency resolution
- Better error messages
- More reliable solving for complex environments
- Default in conda 23.10+

### CI/CD Best Practices

**In CI pipelines:**

```yaml
- name: Setup Conda
  uses: conda-incubator/setup-miniconda@v2
  with:
    environment-file: environment.yml
    activate-environment: myproject
    use-mamba: true  # Use mamba for faster installs

- name: Install from lockfile (deterministic)
  run: |
    conda activate myproject
    conda-lock install --name myproject conda-lock.yml

- name: Run tests
  run: |
    conda activate myproject
    $(which python) -m pytest tests/
```

**Best Practices:**
- Use lockfiles for deterministic installs (`conda-lock install`)
- Run `conda env update -f environment.yml --prune` for clean syncs
- Clean caches periodically: `conda clean --all -y`
- Use `conda-lock` or `pixi` for reproducible CI builds

### Containerizing Conda Environments

**When using Docker/Podman:**

```dockerfile
# Use official conda base image
FROM continuumio/miniconda3:latest

# Copy environment file
COPY environment.yml .

# Create environment
RUN conda env create -f environment.yml

# Activate environment in shell
SHELL ["conda", "run", "-n", "myproject", "/bin/bash", "-c"]

# Set environment as default
ENV PATH /opt/conda/envs/myproject/bin:$PATH

# Your application
COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
```

**Best Practices:**
- Use `conda/miniconda3` or `continuumio/miniconda3` base images
- Activate environments explicitly in Dockerfiles
- Avoid mixing `apt` and `conda` installs unless documented and justified
- Use multi-stage builds to reduce final image size
- Use lockfiles for reproducibility

**Further Reading:**
- [Deploying Conda Environments in Docker - Best Practices](https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html)
- [Shipping conda environments to production using pixi](https://tech.quantco.com/blog/pixi-production)

---

## Common Conda Commands

```bash
# List all environments
conda env list
conda info --envs

# Create new environment
conda create -n myenv python=3.11

# Clone existing environment
conda create -n myclone --clone myenv

# Remove environment
conda env remove -n myenv

# Search for packages
conda search <package-name>
conda search -c conda-forge <package-name>

# Update conda itself
conda update -n base conda

# Update all packages in environment
conda update --all

# Clean up unused packages/cache
conda clean --all

# List installed packages
conda list

# List installed packages with source
conda list --show-channel-urls

# Export environment (concise)
conda env export --from-history > environment.yml

# Export environment (full)
conda env export > environment-full.yml

# Show environment info and virtual packages
conda info

# Show configuration
conda config --show

# Set channel priority
conda config --set channel_priority strict
```

---

## Quick Reference: Common Workflows

### Starting a New Project

```bash
# 1. Create environment
conda create -n myproject python=3.11
conda activate myproject

# 2. Install core dependencies
conda install numpy pandas scikit-learn jupyter

# 3. Install pure-Python packages
pip install requests flask

# 4. Export environment
conda env export --from-history > environment.yml

# 5. Create lockfile for reproducibility
conda-lock -f environment.yml -p linux-64

# 6. Commit to version control
git add environment.yml conda-lock.yml
git commit -m "Add project environment"
```

### Reproducing an Environment

```bash
# From environment.yml (with solving)
conda env create -f environment.yml

# From lockfile (deterministic)
conda-lock install --name myproject conda-lock.yml

# Verify
conda activate myproject
$(which python) --version
conda list
```

### Updating Dependencies

```bash
# Update specific packages
conda update numpy pandas

# Update all packages
conda update --all

# Update from environment.yml
conda env update -f environment.yml --prune

# Regenerate lockfile
conda-lock -f environment.yml -p linux-64

# Test thoroughly, then commit
git add environment.yml conda-lock.yml
git commit -m "Update dependencies"
```

---

## Testing and Linting

**Always use full paths for test runners and linters:**

```bash
# ✅ CORRECT - Full path to test runner
/opt/miniconda3/envs/myproject/bin/pytest tests/
/opt/miniconda3/envs/myproject/bin/python -m pytest tests/

# ✅ CORRECT - Full path to linters
/opt/miniconda3/envs/myproject/bin/black src/
/opt/miniconda3/envs/myproject/bin/mypy src/
/opt/miniconda3/envs/myproject/bin/ruff check .

# ✅ CORRECT - Using which to get path dynamically
$(which python) -m pytest
$(which black) src/
```

---

## Troubleshooting

### "Command not found" errors

**Problem:** Command not found after installing package

**Solution:** Use full path to the binary:
```bash
# Instead of:
pytest

# Use:
/opt/miniconda3/envs/myproject/bin/pytest

# Or:
$(which pytest)
```

### Environment not activating

**Problem:** `conda activate` not working

**Solution:** Initialize conda for your shell:
```bash
conda init bash  # or zsh, fish, powershell, etc.
# Restart shell
```

### Conflicting dependencies

**Problem:** Conda can't resolve dependencies

**Solutions:**
1. Try installing packages one at a time
2. Use `conda-forge` channel
3. Create fresh environment
4. Use `mamba` (faster conda replacement): `conda install mamba -c conda-forge`
5. Check for conflicting channel specifications

### "This environment is externally managed"

**Problem:** On some systems (Ubuntu 23.04+), pip is restricted by PEP 668

**Solution:** Always use conda environments:
```bash
# ❌ This may fail on newer systems
pip install package

# ✅ Always use conda environment
conda create -n myproject python=3.11
conda activate myproject
pip install package  # Now pip is safe inside conda
```

### Slow solver / hanging installs

**Problem:** Dependency resolution takes too long

**Solutions:**
```bash
# Use libmamba solver (much faster) 
# NOTE: YOU DO NOT NEED TO INSTALL THIS AS LONG AS USER HAS AN UPDATED CONDA
conda install -n base conda-libmamba-solver
conda config --set solver libmamba

# Use mamba instead of conda
conda install mamba -c conda-forge
mamba install <package>

# Use pixi (modern, fastest)
pixi add <package>
```

### Mixed conda/pip packages causing issues

**Problem:** Environment broken after mixing conda and pip

**Best practice:**
1. Always install conda packages first
2. Then install pip packages
3. Document the order in `environment.yml`
4. Avoid re-running conda install after pip

**If environment is broken:**
```bash
# Recreate from scratch
conda env remove -n myproject
conda env create -f environment.yml
```

---

## Common Misconceptions About Conda

### ❌ "Conda is only for data science"
**Reality:** Conda packages cover web frameworks (flask, fastapi), databases (postgresql, redis), cloud tools (aws-cli, terraform), system utilities, and DevOps tooling. It's a general-purpose distribution system.

### ❌ "Conda is slow"
**Reality:** Modern solvers (libmamba, mamba) are 10-100x faster than old conda. The classic solver was slow; the ecosystem has evolved dramatically.

### ❌ "Conda environments are huge"
**Reality:** Because conda doesn't ship `glibc` (on Linux) or full OS userspace, environments are typically hundreds of MB *smaller* than equivalent Docker containers with similar functionality.

### ❌ "I should use pip for everything"
**Reality:** Pip is excellent for pure-Python packages. But for anything with compiled extensions or native dependencies, conda provides better performance, reliability, and cross-platform consistency.

### ❌ "Conda replaces Docker"
**Reality:** They're complementary. Put conda environments *inside* Docker containers for the best of both:
- Docker: Process isolation, deployment consistency, system-level isolation
- Conda: Environment reproducibility, dependency solving, binary optimization

### ❌ "Anaconda and conda are the same thing"
**Reality:** 
- **conda**: The package manager and environment management tool
- **Anaconda**: A distribution that includes conda plus 250+ pre-installed packages
- **Miniconda**: Minimal installer with just conda and Python
- **Anaconda, Inc.**: The company (where you work!)

### ❌ "environment.yml is enough for reproducibility"
**Reality:** `environment.yml` specifies version *ranges*. For true reproducibility, you need lockfiles that capture exact versions and hashes. Use `conda-lock` or `pixi`.

---

## Internal Policy Summary

**10 Commandments for Anaconda Conda Development:**

1. 🥇 **Conda first** — defaults channel, then conda-forge, pip last
2. 📦 **Environments only** — never global installs, always isolated environments
3. 🔒 **Lock it** — use conda-lock for reproducibility in production
4. 🧠 **Full paths, always** — explicit > implicit (use full Python paths)
5. 🧮 **Binary builds > source builds** — speed + reliability + optimization
6. 🧰 **Use conda for tooling**, not just Python libs (kubectl, terraform, etc.)
7. ⚙️ **libmamba solver by default** — fast, reliable, better error messages
8. 📝 **Document pip installs** in `environment.yml` under `pip:` section
9. 🚫 **No venv** unless explicitly justified for specific use cases
10. 🧾 **Commit `environment.yml` + lockfiles** to version control

---

## Conda's Rolling Distribution Model

Unlike operating systems with fixed releases (Ubuntu 24.04, RHEL 9, etc.), conda is a **rolling distribution**:
- Packages are continuously updated
- No "version upgrades" needed
- Migration infrastructure rebuilds dependent packages automatically

### What This Means For You

When a core library updates (e.g., OpenSSL 3.0 → 4.0), conda-forge automatically:
1. Identifies all dependent packages
2. Rebuilds them in correct dependency order
3. Ensures binary (ABI) compatibility
4. Publishes new builds

**Result:** Your environments can stay current without breaking changes.

**Best Practice:** Use lockfiles to control when you adopt updates:
```bash
# Lock current working environment
conda env export --from-history > environment.yml
conda-lock -f environment.yml

# Update when you're ready
conda-lock --update numpy scipy
# Test thoroughly, then commit the updated lock
```

This continuous rebuilding maintains ABI compatibility as dependencies evolve across Linux, macOS, and Windows—something traditional distributions can't easily achieve.

---

## Additional Resources

### Official Documentation
- [Conda User Guide](https://docs.conda.io/projects/conda/en/stable/user-guide/index.html)
- [conda-forge Documentation](https://conda-forge.org/docs/)
- [conda-lock Documentation](https://conda.github.io/conda-lock/)
- [pixi Documentation](https://pixi.sh/)

### Understanding Conda (conda.org Blog Series)
- [Part 1: Conda ≠ PyPI](https://conda.org/blog/conda-is-not-pypi)
- [Part 2: Conda in the Packaging Spectrum](https://conda.org/blog/conda-pip-docker-nix)
- [Part 3: Practical Power](https://conda.org/blog/conda-practical-power/)

### Best Practices
- [Deploying Conda in Docker](https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html)
- [PyPackaging Native (ABI challenges)](https://pypackaging-native.github.io/)

---

*This is the official Anaconda internal development standard.*
*For Anaconda developers using Claude Code and AI coding assistants.*
*Last updated: 2025-11-13*


---

<!-- Auto-generated by Anaconda Claude Code Launcher -->
<!-- Source: ~/.anaconda-claude-code/claude-instructions.md -->
<!-- Generated: criteria_checker project -->
<!-- To update: Use "Manage Instructions" in launcher -->
