# Copyright 2024 The AI Edge Torch Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from jax._src.lib.mlir import ir
from jax._src.lib.mlir import passmanager


def run_pass(pipeline, module: ir.Module):
  pm = passmanager.PassManager.parse(pipeline)
  pm.run(module.operation)
  return module


def canonicalize(module: ir.Module):
  return run_pass("builtin.module(canonicalize)", module)


def cse(module: ir.Module):
  return run_pass("builtin.module(cse)", module)


def inline(module: ir.Module):
  return run_pass("builtin.module(inline)", module)


def strip_debuginfo(module: ir.Module):
  return run_pass("builtin.module(strip-debuginfo)", module)
