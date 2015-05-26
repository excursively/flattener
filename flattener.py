# -*- coding: utf-8 -*-

class flattener(object):

    def flatten(self, data, prefix=""):
        valuedict = dict()

        if type(data) is dict:
            for key in data:
                dictdata = data[key]
                if prefix == "":
                    newprefix = key
                else:
                    newprefix = prefix + "__" + key

                returndict = self.flatten(dictdata, newprefix)
                valuedict.update(returndict)

            return valuedict

        else:
            keyname = prefix
            valuedict[keyname] = data

            return valuedict
