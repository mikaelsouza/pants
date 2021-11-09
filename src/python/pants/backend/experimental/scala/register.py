# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.backend.java.package import deploy_jar  # TODO: Should move to the JVM package.
from pants.backend.java.target_types import (  # TODO: All of these should move to the JVM package.
    DeployJar,
    JunitTestsGeneratorTarget,
    JunitTestTarget,
)
from pants.backend.java.test import junit  # TODO: Should move to the JVM package.
from pants.backend.scala.compile import scalac
from pants.backend.scala.dependency_inference import scala_parser
from pants.backend.scala.goals import check
from pants.backend.scala.target_types import ScalaSourcesGeneratorTarget, ScalaSourceTarget
from pants.backend.scala.target_types import rules as target_types_rules
from pants.jvm import classpath, jdk_rules
from pants.jvm import util_rules as jvm_util_rules
from pants.jvm.goals import coursier
from pants.jvm.resolve import coursier_fetch, coursier_setup
from pants.jvm.target_types import JvmArtifact, JvmDependencyLockfile


def target_types():
    return [
        DeployJar,
        ScalaSourceTarget,
        ScalaSourcesGeneratorTarget,
        JunitTestTarget,
        JunitTestsGeneratorTarget,
        JvmArtifact,
        JvmDependencyLockfile,
    ]


def rules():
    return [
        *scalac.rules(),
        *check.rules(),
        *classpath.rules(),
        *junit.rules(),
        *deploy_jar.rules(),
        *coursier.rules(),
        *coursier_fetch.rules(),
        *coursier_setup.rules(),
        *jvm_util_rules.rules(),
        *jdk_rules.rules(),
        *scala_parser.rules(),
        *target_types_rules(),
    ]
