def write_new_file_imp1(ctx):
    output_file = ctx.actions.declare_file(ctx.attr.out_file_name + ".txt")

    ctx.actions.run(
        outputs = [output_file],
        executable = "cmd.exe",
        arguments = ["/c", "type", ctx.file.my_input_file.path, ">>", output_file.path],
    )

    return DefaultInfo(files = depset([output_file]))

write_new_file = rule(
    implementation = write_new_file_imp1,
    attrs = {
        "my_input_file": attr.label(allow_single_file = True),
        "out_file_name": attr.string(),
    },
)
