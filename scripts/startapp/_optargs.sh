#!/bin/bash
############################################################
# Help                                                     #
############################################################
Help() {
    # Display Help
    echo "Creating Django App"
    echo
    echo "Syntax: app_name [-h|-t]"
    echo "options:"
    echo "-h     Print this Help."
    echo "-t     ModelAdmin will be TranslationModelAdmin"
    echo
}
translation=false
############################################################
# Process the input options. Add options as needed.        #
############################################################
# Get the options
for arg in "$@"; do
    if [ "$arg" = "-h" ]; then
        Help
    fi

    if [ "$arg" = "-t" ]; then
        export translation=true
    fi

done
