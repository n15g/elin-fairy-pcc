import os
import shutil

from invoke import task

from lib import project
from lib.console import log_call
from lib.project import config


@task
def version(cmd):
    print(config.version)


@task
@log_call
def clean(cmd):
    project.rmdir(config.build_dir)


@task
@log_call
def prepare_build(cmd):
    project.mkdir(config.package_build_dir)


@task(pre=[clean, prepare_build])
@log_call
def build_actor(cmd):
    project.glob_copy(config.src_dir, "Actor/**/*.png", config.package_build_dir)


@task(pre=[clean, prepare_build])
@log_call
def build_portrait(cmd):
    project.glob_copy(config.src_dir, "Portrait/**/*.png", config.package_build_dir)


@task(pre=[clean, prepare_build])
@log_call
def build_template(cmd):
    project.glob_copy(config.src_dir, "Template/*.json", config.package_build_dir, ".txt")
    project.glob_copy(config.src_dir, "Template/*.bat", config.package_build_dir)


@task(pre=[clean, prepare_build])
@log_call
def build_meta(cmd):
    project.copy_file(os.path.join(config.src_dir, "preview.jpg"), config.package_build_dir)
    project.copy_file(os.path.join(config.root, "README.md"), config.package_build_dir)
    project.copy_file(os.path.join(config.root, "LICENSE"), config.package_build_dir)


@task(pre=[clean, prepare_build])
@log_call
def build_package_xml(cmd):
    project.copy_template(os.path.join(config.src_dir, "package.xml"), config.package_build_dir)


@task(pre=[build_actor, build_portrait, build_template, build_meta, build_package_xml], default=True)
@log_call
def build(cmd):
    pass


@task(pre=[build])
@log_call
def install(cmd, path: str = config.install_dir):
    package_install_dir = os.path.join(os.path.abspath(path), config.package_name)
    project.rmdir(package_install_dir)
    shutil.copytree(config.package_build_dir, package_install_dir, dirs_exist_ok=True)
    print(f"Installed: {package_install_dir}")


@task
@log_call
def install_templates(cmd, path: str = config.install_template_dir):
    template_dir = os.path.abspath(path)
    project.glob_copy(os.path.join(config.src_dir, "Template"), "*.json", template_dir, ".txt")
    print(f"Installed: {template_dir}")


@task
def clean_dist(cmd):
    project.rmdir(config.dist_dir)


@task
@log_call
def prepare_dist(cmd):
    project.mkdir(config.dist_dir)


@task(pre=[build, clean_dist, prepare_dist])
@log_call
def dist(cmd):
    bundle_name = f"{config.package_name}-v{config.version}"
    bundle_path = os.path.join(config.dist_dir, bundle_name)
    project.mkarchive(config.build_dir, bundle_path)
