class Dockerfile:
	def __init__(self, baseimage, init=''):
		self.baseimage = baseimage
		self.copy_files = []
		self.run_commands = []
		self.expose_ports = []
		self.env = []
		self.cmd = ""
		self.entrypoint = ""
		self.init = init

	def add_file(self, f):
		self.copy_files.append(f)

	def add_run_command(self,cmd):
		self.run_commands.append(cmd)

	def add_expose_port(self, p):
		self.expose_ports.append(p)

	def add_env(self, env):
		self.env.append(env)

	def set_cmd(self,cmd):
		self.cmd=cmd

	def set_entrypoint(self,e):
		self.entrypoint=e

	def add_to_dockerfile(self,dockerfile, cmd, lst):
		for l in lst:
			dockerfile+=cmd + " " + l + "\n"
		return dockerfile

	def create_dockerfile(self):

		if self.init:
			dockerfile = self.init
		else:
			dockerfile = "FROM " + self.baseimage + "\n"
		
		dockerfile = self.add_to_dockerfile(dockerfile, "COPY", self.copy_files)
		dockerfile = self.add_to_dockerfile(dockerfile, "RUN", self.run_commands)
		dockerfile = self.add_to_dockerfile(dockerfile, "EXPOSE", self.expose_ports)
		dockerfile = self.add_to_dockerfile(dockerfile, "ENV", self.env)

		if self.entrypoint:
			dockerfile = self.add_to_dockerfile(dockerfile, "ENTRYPOINT", [self.entrypoint])
		elif self.cmd:
			dockerfile = self.add_to_dockerfile(dockerfile, "CMD", self.cmd)

		return dockerfile