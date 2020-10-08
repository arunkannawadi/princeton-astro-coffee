# -*- coding: utf-8 -*-

'''This contains the main Astro-Coffee URL handlers.

'''

#############
## LOGGING ##
#############

import logging
LOGGER = logging.getLogger(__name__)

LOGDEBUG = LOGGER.debug
LOGINFO = LOGGER.info
LOGWARNING = LOGGER.warning
LOGERROR = LOGGER.error
LOGEXCEPTION = LOGGER.exception


#############
## IMPORTS ##
#############

from . import basehandler


#########################
## BASIC PAGE HANDLERS ##
#########################

class LoginHandler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class LogoutHandler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class NewUserHandler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class VerifyUserHandler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class ForgotPassStep1Handler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class ForgotPassStep2Handler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class ChangePassHandler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )


class DeleteUserHandler(basehandler.BaseHandler):

    def get(self):
        '''
        This handles the basic index page.

        '''

        flash_message_list, alert_type = self.get_flash_messages()

        self.render(
            'index.html',
            baseurl=self.conf.base_url,
            current_user=self.current_user,
            conf=self.conf,
            page_title='Astro-Coffee@%s' % self.conf.institution,
            flash_message_list=flash_message_list,
            alert_type=alert_type,
        )
