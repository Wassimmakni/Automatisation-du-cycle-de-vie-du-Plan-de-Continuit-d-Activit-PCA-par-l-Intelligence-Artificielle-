def classifier_processus(processus):

    processus = processus.lower()

    if "paie" in processus:
        return "5"

    if "vente" in processus:
        return "4"

    return "2"